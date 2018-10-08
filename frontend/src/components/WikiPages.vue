<template>
  <div class="container">
    <div
      class="alert alert-dark"
      role="alert">
      <b-btn
        v-b-modal.addWikiPage
        variant="primary">
        Add WikiPage
      </b-btn>
      <span class="float-right">Number of WikiPages: {{ wikipages_count }}</span>
    </div>
    <div
      v-for="page in pages"
      class="pt-3">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ page.title }}</h5>
          <p class="card-subtitle mb-2 text-muted">Created at {{ page.created_at }}
            <span
              v-if="page.is_updated"
              class="text-info"
              style="float:right"> Updated at {{ page.updated_at }}
            </span>
          </p>
          <p class="card-text">{{ page.text }}</p>
          <b-btn
            v-b-modal.updateWikiPage
            size="sm"
            variant="warning"
            @click="sendInfo(page)">
            Edit WikiPage
          </b-btn>
        </div>
      </div>
    </div>

    <div>
      <b-modal
        id="addWikiPage"
        ref="addModal"
        title="Add WikiPage"
        @ok="handleAddOk"
        @shown="clearValues">
        <form @submit.stop.prevent="handleAddSubmit">
          <div class="pt-4">
            <b-form-input
              type="text"
              placeholder="Enter Title"
              v-model="title">
            </b-form-input>
          </div>
          <div class="pt-4">
            <b-form-textarea
              v-model="text"
              :rows="10"
              :max-rows="100"
              placeholder="Enter Text">
            </b-form-textarea>
          </div>
        </form>
      </b-modal>
    </div>

    <div>
      <b-modal
        id="updateWikiPage"
        ref="updateModal"
        title="Edit WikiPage"
        @ok="handleUpdateOk">
        <form @submit.stop.prevent="handleUpdateSubmit">
          <div class="pt-4">
            <b-form-input
              type="text"
              placeholder="Enter Title"
              v-model="title">
            </b-form-input>
          </div>
          <div class="pt-4">
            <b-form-textarea
              v-model="text"
              :rows="10"
              :max-rows="100"
              placeholder="Enter Text">
            </b-form-textarea>
          </div>
        </form>
      </b-modal>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  const API_URL = 'http://0.0.0.0:8000/api/wikipages';

  export default {
    name: 'WikiPages',
    data() {
      return {
        pages: [],
        title: '',
        text: '',
        page_id: '',
        page_url: '',
        current_page: ''
      }
    },
    computed: {
      wikipages_count: function() {
        return this.pages.length
      },
    },
    mounted: function() {
      this.getWikiPages()
    },
    methods: {
      getWikiPages: function() {
        axios.get(API_URL)
          .then(response => {
            console.log(response.data);
            this.pages = response.data
          })
          .catch(error => {
            console.log(error);
          });
      },
      sendInfo: function(page) {
        this.title = page.title;
        this.text = page.text;
        this.page_id = page.id;
        this.page_url = API_URL + '/' + page.id;
        this.current_page = page

      },
      clearValues: function() {
        this.title = '';
        this.text = '';
        this.page_id = '';
        this.page_url = ''
      },
      handleAddOk: function(evt) {
        // Prevent modal from closing
        evt.preventDefault();
        if (!this.title || !this.text) {
          alert('Please enter title and text')
        } else {
          this.handleAddSubmit()
        }
      },
      handleAddSubmit: function() {
        axios.post(API_URL, {
          title: this.title,
          text: this.text
        })
          .then(response => {
            this.pages.unshift(response.data);
            alert('Saved' + '  ' + response.data.title)
          })
          .catch(error => {
            console.log(error);
          });
        this.clearValues();
        this.$refs.addModal.hide()
      },
      handleUpdateOk: function(evt) {
        // Prevent modal from closing
        // debugger
        evt.preventDefault();
        if (!this.title || !this.text) {
          alert('Please enter title and text')
        } else {
          this.handleUpdateSubmit()
        }
      },
      handleUpdateSubmit: function() {
        axios.put(this.page_url, {
          title: this.title,
          text: this.text
        })
          .then(response => {
            this.current_page.text = response.data.text;
            this.current_page.title = response.data.title;
            this.current_page.updated_at = response.data.updated_at;
            this.current_page.is_updated = response.data.is_updated;
            alert('Updated' + '  ' + response.data.title)
          })
          .catch(error => {
            console.log(error)
          });
        this.clearValues();
        this.$refs.updateModal.hide()
      }
    },
  }
</script>

<style lang="scss" scoped>
  h1 {
    text-align: left;
  }
</style>
