### The Movie App

> Everything deserves an app!
>
> -- <cite>Benjamin Franklin</cite>

You are building an app for people to go see movies at your local movie theater. Luckily and API is available to call and get movie titles and show times from. All you need to do now is fetch all the data. Simple enough.

### Requirements
- Fetch title of a movie using its id.
  - `/movie-title/{movie_id}/`
- Fetch show times for a single movie for the entire week.
  - `/show-time/{movie_id}/{day}/`
- Make this fetching of show times performant. Somehow.
- Fetch show times for all 10 movies.
- ???
- Maybe do error handling?
  - `/movie-title/{movie_id}/?q=flaky`
  - `/show-time/{movie_id}/{day}/?q=flaky`

### This week's movie Ids
```txt
10954600
338526
120347
6710474
120737
88763
78748
120735
88247
377092
```
