### GeekBrains Django course
### Project end-points:
#### Lections
    1. myapp
        http://127.0.0.1:8000/prefix/
        http://127.0.0.1:8000/prefix/about/

    2. myapp2
        add custom commands in /myapp2/management/commands/*crud to work with cli

    3. myapp3
        http://127.0.0.1:8000/les3/hello/
        http://127.0.0.1:8000/les3/hello2/
        http://127.0.0.1:8000/les3/posts/<int:year>/
        http://127.0.0.1:8000/les3/posts/<int:year>/<int:month>/
        http://127.0.0.1:8000/les3/posts/<int:year>/<int:month>/<slug:slug>/
        http://127.0.0.1:8000/
        http://127.0.0.1:8000/les3/if/
        http://127.0.0.1:8000/les3/for/
        http://127.0.0.1:8000/les3/index/
        http://127.0.0.1:8000/les3/about/
        http://127.0.0.1:8000/les3/author/<int:author_id>/
        http://127.0.0.1:8000/les3/post/<int:post_id>/

    4. myapp4
        http://127.0.0.1:8000/les4/user/add/
        http://127.0.0.1:8000/les4/forms/
        http://127.0.0.1:8000/les4/user/
        http://127.0.0.1:8000/les4/upload/

    5. myapp5
        add admin panel views, search filters and couple users

    6. myapp6
        add django-debug-toolbar, compare db queries with profiling
        prepare project to cloud deploy and deploying to www.pythonanywhere.com

#### Seminars
    1. s1_app
        http://127.0.0.1:8000/seminar1/

       s1_game_app
        http://127.0.0.1:8000/seminar1/heads_and_tails/
        http://127.0.0.1:8000/seminar1/roll_the_dice/
        http://127.0.0.1:8000/seminar1/random_number/
    
    2. s2_app1_coin_app
        http://127.0.0.1:8000/seminar2/heads_and_tails/
        http://127.0.0.1:8000/seminar2/heads_and_tails/stats/<n:int>
       
       s2_app2_article_app
        add custom commands in /s2_app2_article_app/management/commands/*crud to work with cli
        http://127.0.0.1:8000/seminar2/articles_by_author_firstname/<author_firstname>
        http://127.0.0.1:8000/seminar2/articles_by_author_firstname/<author_firstname>/<max_results>/
        http://127.0.0.1:8000/seminar2/articles_by_author_firstname/<author_firstname>/<max_results>/<filter_by>
        http://127.0.0.1:8000/seminar2/comments_by_author_firstname/<author_firstname>
        http://127.0.0.1:8000/seminar2/comments_by_article_title/<article_title>

    3. s3_app1_app
        http://127.0.0.1:8000/seminar3/
        http://127.0.0.1:8000/seminar3/about/
       
       s3_app2_game_app 
        http://127.0.0.1:8000/seminar3/heads_and_tails/
        http://127.0.0.1:8000/seminar3/roll_the_dice/
        http://127.0.0.1:8000/seminar3/random_number/
        
       s3_app3_article_app
        http://127.0.0.1:8000/seminar3/articles_by_author_id/<int:author_id>
        http://127.0.0.1:8000/seminar3/article_by_id/<int:article_id>
        http://127.0.0.1:8000/seminar3/article_stats_by_id/<int:article_id>
       
    4. s4_app1_game_app
        http://127.0.0.1:8000/seminar4/heads_and_tails/
        http://127.0.0.1:8000/seminar4/roll_the_dice/
        http://127.0.0.1:8000/seminar4/random_number/

       s4_app2_article_app
        http://127.0.0.1:8000/seminar4/author/new
        http://127.0.0.1:8000/seminar4/article/new
        http://127.0.0.1:8000/seminar4/article_by_id/<int:article_id>

    5. s5_admin_app
        add admin panel configuration for s4_app2_article_app

#### Homework
    1. hw1_app
        http://127.0.0.1:8000/homework1/
        http://127.0.0.1:8000/homework1/about

    2. hw2_app
        add models acording to the task 
        add custom commands in /hw2_app/management/commands/*crud to work with cli

    3. hw3_app
        http://127.0.0.1:8000/homework3/customer/<int:customer_id>/orders/
	    http://127.0.0.1:8000/homework3/customer/<int:customer_id>/stats/
	    http://127.0.0.1:8000/homework3/customer/<int:customer_id>/stats/<int:scope_in_days>/

    4. hw4_app
        http://127.0.0.1:8000/homework4/product/new
        http://127.0.0.1:8000/homework4/product/<int:product_id>/edit

    5. hw5_app
        add admin panel configuration for hw4_app models