<template>
  <div class="about-me-container row items-center">
    <div class="col-8 q-pl-xl q-pr-md">
      <h2>Ethan Yan</h2>
      <p>
        Hello! I'm Ethan, a passionate developer with experience in various
        modern web technologies. I love building efficient and user-friendly
        applications that solve real-world problems. When I'm not coding, you
        can find me running, eating, or exploring new technologies.
      </p>

      <p>
        This site is mainly used as a submission for Fetch where I have applied
        for the Frontend, Backend, Machine Learning, and Data Engineering
        Internship roles.
      </p>

      <div class="social-media-icons row q-mt-md">
        <a
          href="https://www.linkedin.com/in/ethan-yan-20a71b205/"
          target="_blank"
          class="q-mr-md"
        >
          <img
            src="https://www.google.com/s2/favicons?domain=linkedin.com"
            alt="LinkedIn Icon"
          />
        </a>
        <a href="https://github.com/ethanyan" target="_blank">
          <img
            src="https://www.google.com/s2/favicons?domain=github.com"
            alt="GitHub Icon"
          />
        </a>
      </div>
    </div>

    <div class="col-4">
      <div class="profile-photo-container">
        <q-img
          src="src/assets/ethan-yan-photo.jpg"
          alt="Ethan Yan"
          class="profile-photo"
          :fit="'cover'"
        >
          <div class="absolute-bottom text-subtitle1 text-center">
            SEA Games 2022
          </div>
        </q-img>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.about-me-container {
  justify-content: space-between;
}

h2 {
  font-size: 3em;
  font-weight: bold;
}

p {
  font-size: 1em;
  margin-top: 1em;
}

.social-media-icons img {
  width: 32px;
  height: 32px;
  margin-right: 15px;
}
.profile-photo-container {
  width: 100%;
  height: 600px; /* or a fixed height like 300px if you prefer */
  overflow: hidden; /* important to hide overflow if the image gets cropped */
  position: relative; /* relative position to position the child image */
}

.profile-photo {
  display: block; /* remove any default spacing */
  min-width: 100%;
  min-height: 100%;
  position: absolute; /* to allow for centering */
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  object-fit: contain; /* important to ensure the image scales and covers */
}
</style>
