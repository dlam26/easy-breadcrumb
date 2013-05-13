

    *Easy Breadcrumb!*

Build a "navigation breadcrumb" by just typing its contents on separate lines.

Example::
    <div class="breadcrumbs with-urls">

        {% with foxnews_url="http://foxnews.com"  trolling_url="http://en.wikipedia.org/wiki/Troll_(Internet)" %}
            {% breadcrumb %}

                Yahoo   -|-          http://yahoo.com
              Fox News  -|-   {{ foxnews_url }}
              trolling  -|-                     {{ trolling_url }}

            {% endbreadcrumb %}
        {% endwith %}
    </div>

turns into this HTML...::

    <div class="breadcrumbs with-urls">

        <li ><span class="caret">&raquo;</span> <a href="http://yahoo.com">Yahoo</a></li>
        <li ><span class="caret">&raquo;</span> <a href="http://foxnews.com">Fox News</a></li>
        <li ><span class="caret">&raquo;</span> <a href="http://en.wikipedia.org/wiki/Troll_(Internet)">trolling</a></li>

    </div>
    
