import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aanandita's Top 6 (Not Scary) Halloween Movies</title>
    <link rel="icon" href="assets/pumpkin_light.png">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,700|Oswald:700" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            color: #3c3c3c;
            font-family: 'Montserrat', Helvetica, Arial, sans-serif;
        }
        .container { width: 100%; padding: 0; }
        .container > .navbar-header { margin: 0; }
        h2,h4 { margin: 0; color: #3c3c3c }
        h2 { font-family: 'Oswald', sans-serif; font-size: 32px; font-weight: 700; line-height: 42px; }
        h4 { font-size: 18px; font-weight: 500; line-height: 24px; letter-spacing: -0.5px; }
        p { padding: 0; margin: 0; line-height: 20px; }

        .navbar { position: static; margin-bottom: 60px; }
        .navbar-header { float: none; }
        .navbar .navbar-brand { color: #fff; text-shadow: none; height: auto; float: none; padding: 10px 15px; display: block; text-align: center; }
        .navbar .navbar-brand img { width: 56px; height: 56px; display: inline-block; vertical-align: middle; margin-right: 5px; }
        .navbar .navbar-brand .page-title { text-transform: uppercase; display: inline-block; vertical-align: middle; font-size: 24px; font-weight: 700; line-height: 28px; }
        .navbar .navbar-brand .page-title span { font-weight: 400; }
        .main-content { width: 100%; max-width: 1000px; }

        #trailer .modal-dialog {
            /* margin-top: 200px; */
            width: 100%;
            height: 100vh;
            padding: 20px;
            margin: 0;
        }
        #trailer .modal-dialog .modal-content {
            width: 100%;
            height: 100%;
            background-size: cover;
            background-repeat: no-repeat;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
        }
        .movie-tile {
            /* min-height: 458px; */
            width: 100%;
            max-width: 840px;
            margin: 0 auto 60px;
            float: none;
        }
        .flex-box { display: flex; padding: 0 20px; }
        .flex-box .flex-left { float: left; width: 220px; flex: 0 0 220px; margin-right: 40px; }
        .flex-box .flex-right { float: right; }
        .flex-box .flex-right .btn-container { margin-top: 30px; }
        .flex-box .flex-right .btn-container a { padding: 10px; background: #3c3c3c; color: #fff; border-radius: 2px; font-size: 12px; text-transform: uppercase; }
        .flex-box .flex-right .btn-container a:hover, .flex-box .flex-right .btn-container a:focus { text-decoration: none; background: #282828; }
        .flex-box .flex-right .btn-container a i { margin-right: 4px; }
        .movie-tile span { font-size: 14px; display: block; padding: 20px 0; }
        .movie-tile img {
            /* cursor: pointer; */
        }
        .rating-container .rect { width: 100%; height: 20px; border: 1px solid #f5f5f5; background: #fff; }
        .rating-container .rect .rating {
            display: block;
            position: relative;
            background: linear-gradient(to right, #ffffff, #FF8E47);
            background: -webkit-linear-gradient(left, #ffffff, #FF8E47);
            height: 100%;
        }
        .rating-container .rect .rating:after {
            position: absolute;
            bottom: -46px;
            right: -35px;
            content: attr(data-rating-hover);
            padding: 10px 0;
            width: 70px;
            text-align: center;
            border-radius: 2px;
            background: #3c3c3c;
            color: #fff;
            visibility: hidden;
            opacity: 0;
        }
        .rating-container .rect .rating:before {
            position: absolute;
            width: 0;
            height: 0;
            transform: rotate(180deg);
            bottom: -6px;
            right: -6px;
            content: "";
            border-style: solid;
            border-width: 6px 6px 0 6px;
            border-color: #3c3c3c transparent transparent transparent;
            visibility: hidden;
            opacity: 0;
        }
        .animate {
            -webkit-transition: all 0.2s ease-in-out;
            -moz-transition: all 0.2s ease-in-out;
            -ms-transition: all 0.2s ease-in-out;
            -o-transition: all 0.2s ease-in-out;
            transition: all 0.2s ease-in-out;
        }
        .rating-container .rect .rating:hover:before, .rating-container .rect .rating:hover:after { visibility: visible; opacity: 1; }
        .movie-tile .mobile-info { position: absolute; padding: 0; right: 5px; top: 50%; transform: translateY(-50%); display: inline-block; font-size: 12px; display: none; color: #fff; }
        .video-width-container{ max-width: 600px; margin: 0 auto; height: 100%; position: relative; }
        .scale-media {
            padding-bottom: 56.25%;
            position: absolute;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 600px;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
        }
        @media screen and (max-width: 768px) {
            .flex-box { padding: 0; }
            .movie-tile .mobile-info { display: inline-block; }
            .rating-container .rect .rating:hover:before, .rating-container .rect .rating:hover:after, .rating-container .rect .rating:hover:before, .rating-container .rect .rating:hover:after { visibility: hidden; opacity: 0; }
        }
        @media screen and (max-width: 767px) {
            .flex-box { display: block; }
            .flex-box .flex-left, .flex-box .flex-right { float: none; }
            .flex-box .flex-left { width: 100%; max-width: 400px; margin: 0 auto 10px; }
            .flex-box .flex-left img { width: 100%; height: 100%; }
            .flex-box .flex-right { max-width: 400px; margin: 0 auto; padding: 0 10px; }
        }
        @media screen and (max-width: 650px) {
            .navbar .navbar-brand { padding: 20px 15px; }
            .navbar .navbar-brand img, .navbar .navbar-brand .page-title { display: block; margin: 0 auto; }
            .navbar .navbar-brand img { margin-bottom: 5px; }
        }
        @media screen and (max-width: 450px) {
            #trailer .modal-dialog { height: 400px; margin: 100px 0 0; }
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $('.modal').hide();
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', 'a.modal-open', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            var backdropImageURL = $(this).attr('data-backdrop-url')
            console.log(backdropImageURL)
            $('.modal-content').css({'background-image':'url("' + backdropImageURL + '")'});
        });

        // Animate in the movies when the page loads
        /*
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        */

        // Animate the pumpkin in the header
        $(document).ready(function() {
            if ($(window).width() > 650) {
                $('.navbar-brand').hover(function() {
                    $(this).children('img').attr('src','assets/pumpkin2-candle-.png');
                }, function() {
                    $(this).children('img').attr('src','assets/pumpkin_skull.png');
                });
            }
            else {
                $('.navbar-brand img').attr('src','assets/pumpkin2-candle-.png');
            }
        });
        // Generates a bar to display movie rating
        $(document).ready(function() {
            $('.rect').each(function() {
                var barWidth = $(this).attr('data-rating') / 10
                var containerWidth = $(this).width()
                var totalWidth = barWidth * containerWidth
                $(this).find($('.rating')).width(totalWidth)

                console.log(totalWidth)
                var ratingPercent = ($(this).attr('data-rating') * 10) + '%'
                console.log(ratingPercent)
                $(this).find($('.rating')).attr('data-rating-hover',ratingPercent)
            });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="/" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="video-width-container">
              <div class="scale-media" id="trailer-video-container">
              </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">
                <img src="assets/pumpkin_skull.png" alt="" />
                <span class="page-title">Top 6 <span>(Not Scary)</span> Halloween Movies</span>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="container main-content">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile">
    <div class="flex-box">
        <div class="flex-left">
            <img src="{poster_image_url}" width="220" height="342" class="movie-tile-img">
        </div>
        <div class="flex-right">
            <h2>{movie_title}</h2>
            <h4>{movie_tagline}</h4>
            <span class="storyline">{movie_storyline}</span>
            <div class="rating-container">
                <div class="rect" data-rating="{movie_rating}">
                    <a class="rating animate" data-rating-hover="">
                        <span class="mobile-info">{movie_rating}/10</span>
                    </a>
                </div>
            </div>
            <div class="btn-container">
                <a href="#" class="modal-open" data-trailer-youtube-id="{trailer_youtube_id}" data-backdrop-url="{backdrop_image_url}" data-toggle="modal" data-target="#trailer"><i class="fa fa-youtube-play"></i> Watch Trailer</a>
            </div>
        </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_tagline=movie.tagline,
            movie_rating=movie.rating,
            poster_image_url=movie.poster_image_url,
            backdrop_image_url=movie.backdrop_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
