from application import app
from flask import session, render_template, request, jsonify

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

def _find_blog_posts(page):

  first_post = 101
  per_page = 3
  offset = ((page - 1) * per_page) + 1

  blog_posts = []

  # This is our "fake" database
  for i in range(per_page):

    id = first_post - 1 + offset + i

    blog_post = {
      'id' : id,
      'title' : "Blog Post #{}".format(id),
      'content' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed scelerisque nunc malesuada mauris fermentum commodo. Integer non pellentesque augue, vitae pellentesque tortor. Ut gravida ullamcorper dolor, ac fringilla mauris interdum id. Nulla porta egestas nisi, et eleifend nisl tincidunt suscipit. Suspendisse massa ex, fringilla quis orci a, rhoncus porta nulla. Aliquam diam velit, bibendum sit amet suscipit eget, mollis in purus. Sed mattis ultricies scelerisque. Integer ligula magna, feugiat non purus eget, pharetra volutpat orci. Duis gravida neque erat, nec venenatis dui dictum vel. Maecenas molestie tortor nec justo porttitor, in sagittis libero consequat. Maecenas finibus porttitor nisl vitae tincidunt."
    }

    blog_posts.append(blog_post)

  return blog_posts

# for some reason flask does not accept question mark for get requests
@app.route("/blog-posts/page=<page>")
def return_blog_posts(page):
	page = int(page)
	print(page)

	blog_posts = _find_blog_posts(page)

	res = ""

	for blog_post in blog_posts:

		html = '''
			<div id="blog-post-{0}" class="blog-post">
			  <h3>{1}</h3>
			  <p>{2}</p>
			</div>
		'''.format(*blog_post.values())

		res += html

	return res
