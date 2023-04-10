<template>
  <div class="container">
    <header>
      <h1 class="text-center heading">Repository Viewer</h1>
    </header>
    <br>
    <form @submit.prevent="getProjects">
      <div class="row align-items-end form-group">
        <label for="username" class="text col-md-10 col-sm-10 col-xs-12">GitHub Username:
          <input type="text" class="form-control" id="username" v-model="username">
        </label>
        <button type="submit" class="btn btn-secondary col-md-2 col-sm-2 col-xs-12">Search</button>
      </div>
    </form>
    <hr>
    <div class="row">
      <div class="col-md-6 animate__animated animate__fadeInUp"
      v-for="project in projects" :key="project.id">
        <div class="card mb-4">
          <div class="card-body">
            <h5 class="text card-title"><a target="_blank" :href="project.url">
              {{ project.name }}
            </a></h5>
            <p class="card-text">
              {{ project.description }}
            </p>
            <p v-if="project.language" class="card-text">
              Language: {{ project.language }}
            </p>
            <p v-if="project.topics.length > 0" class="card-text">
              Topics: {{ project.topics.join(', ') }}
            </p>
          </div>
        </div>
      </div>
      <div v-if="projects.length === 0">
        <p class="text">No projects found</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import 'animate.css';

export default {
  name: 'GetProjects',
  data() {
    return {
      username: '',
      projects: [],
    };
  },
  methods: {
    getProjects() {
      const path = `http://localhost:5000/?username=${this.username}`;
      axios.get(path)
        .then((res) => {
          this.projects = res.data;
        })
        .catch((error) => {
          this.error = true;
          this.errorMessage = error.response.data.project || 'An error occurred.';
        });
    },
  },
};
</script>

<style>
@keyframes moveInBottom {
  0% {
    opacity: 0;
    transform: translateY(3 rem);
  }
  100% {
    opacity: 1;
    transform: translate(0);
  }
}
.heading {
  font-family: "Lato", sans-serif;
  font-weight: 400;
  font-style: italic;
}
.text {
  font-family: "Lato", sans-serif;
  font-weight: 300;
  font-size: 1.2rem;
  line-height: 1.7;
}
.card-body {
  height: 10rem;
}
.card {
  box-shadow: 0px 0px 10px 0px rgba(82, 63, 105, 0.1);
}
.card:hover {
  transform: translateY(-3px);
  transition-duration: 500ms;
  box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.2);
}
.card:hover::after {
  transform: scaleX(1.4) scaleY(1.6);
  opacity: 0;
}
.card-text {
  font-family: "Lato", sans-serif;
  font-weight: 100;
}
a, a:link, a:visited, a:hover, a:active {
  color: black !important;
  text-decoration: none;
}
</style>
