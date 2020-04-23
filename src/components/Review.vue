<template>
  <div>
    <h2><em>Review Page</em></h2>
    <br>
    <h3>Movie title</h3>
    <b-form-input class="movie-entry" list="input-list" id="input-with-list" v-model="movie" placeholder="Enter title of movie" ></b-form-input>
    <b-form-datalist id="input-list" :options="movies"></b-form-datalist>
    <br> <br>
    <div class="genre-year">
      <label for="genre">Genre:</label>
      <b-form-input id="genre" v-model="genre" placeholder="Enter genre of movie"></b-form-input>
      <br>
      <label for="year">Year:</label>
      <b-form-input id="year" v-model="year" placeholder="Enter year of movie"></b-form-input>
    </div>
    <br><br>
    <h3>Rating</h3>
    <b-form-select class="movie-rating" v-model="ratingSelected" :options="rating"></b-form-select>
    <br> <br> <br> <br>
    <h3>Review</h3>
    <b-form-textarea
    id="textarea-rows"
    class="textarea"
    placeholder="Tall textarea"
    rows="8"
    v-model="reviewText"
  ></b-form-textarea>
  <br>
  <button @click="onSubmit"> Submit </button>
  <button class="reset" @click="onReset" > Reset </button>

  </div>
</template>

<script>
import axios from "axios";
  export default {
    name: 'create_review_comp',
    props:['curr_user'],
    data() {
      return {
        path: "http://localhost:5000",
        movie: null,
        genre: null,
        year: null,
        ratingSelected: null,
        reviewText: null,
        rating: [
          { value: null, text: 'Please select an option' },
          { value: 1, text: 'Poor(1)' },
          { value: 2, text: 'Below Average(2)' },
          { value: 3, text: 'Average(3)' },
          { value: 4, text: 'Above Average(4)'},
          { value: 5, text: 'Excellent!(5)' }
        ],
        //the movies array will hold the movies contating the matching starting values
        //Ex:Input = S
        //movies[] = ["Scarface", "Scary Movie", "School of Rock"]
        //limit 5 movies
        movieData:{
          movieTitle: null,
          movieGenre: null,
          movieYear: null
        },
        reviewData: {
          movieTitle: null,
          movieReview: null,
          movieComments: null,
          movieRating: null,
          movieGenre: null,
          movieYear: null,
          movieAuthor: null,
          movieDate: null
        }
      }
    },
    methods: {
      onReset(evt){
        this.ratingSelected = null
        this.movie = null
        this.reviewText = null
        this.year = null
        this.genre = null
      },
      onSubmit(evt){
        //set the current date 
        var today = new Date();
        var today = new Date();
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();

        //Start by inserting into movie table
        //First fill movieData obj info
        this.movieData.movieTitle = this.movie
        this.movieData.movieGenre = this.genre
        this.movieData.movieYear = this.year
        axios({
          method: "post",
          url: this.path,
          headers: {
            "Content-type": "application/json"
          },
          data: {
            header: "insert",
            table: "movies",
            content: this.movieData
          }

        }).then(res => {
      });
        //next insert into review table
        //fill reviewData info
        this.reviewData.movieTitle = this.movie
        this.reviewData.movieReview = this.reviewText
        this.reviewData.movieComments = null
        this.reviewData.movieRating = this.ratingSelected
        this.reviewData.movieGenre = this.genre
        this.reviewData.movieYear = this.year
        this.reviewData.movieAuthor = this.curr_user.userName
        this.reviewData.movieDate = date

        axios({
          method: "post",
          url: this.path,
          headers: {
            "Content-type": "application/json"
          },
          data: {
            header: "insert",
            table: "reviews",
            content: this.reviewData
          }
        }).then(res => {
      });
        this.onReset();
      }
    }

  }
</script>

<style>

  #div {
    text-align: center;
  }
  button{
      border:5px solid transparent;
      border-radius: 10px;
      color:white;
      font-size: 20px;
      padding:10px;
      background-color:#af0404;
      margin-left:auto;
      margin-right:auto;

  }

  button:hover{
      opacity: .5;
  }
   .movie-entry, .movie-rating {
    width: 500px;
    margin-left:auto;
    margin-right:auto;
  }

  .textarea{
    width: 1000px;
    margin-left:auto;
    margin-right:auto;
  }
  .reset {
    background-color:#252525;
  }
  .genre-year {
    width: 300px;
    margin: 0 auto;
  }

</style>
