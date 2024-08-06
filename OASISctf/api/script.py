from flask import Flask, request, render_template, jsonify, send_from_directory, abort, session, make_response
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

# Let's assume this is your database of blog posts
blog_posts = [
    {"title": "First Post", "content": "This is the first post."},
    {"title": "Second Post", "content": "This is the second post."},
    # Add more posts as needed...
]

# Dictionary to track progress for each user
user_progress = {}

@app.route('/')
def home():
    token = request.cookies.get('user_token')
    if not token:
        token = str(uuid.uuid4())
        user_progress[token] = {"PATCH": False, "PUT": False, "OPTIONS": False}
        response = make_response(render_template('index.html', posts=blog_posts))
        response.set_cookie('user_token', token)
        return response
    elif token not in user_progress:
        user_progress[token] = {"PATCH": False, "PUT": False, "OPTIONS": False}
    
    return render_template('index.html', posts=blog_posts)
@app.route('/createPost', methods=['POST'])
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')
    if(title == "" and content == ""):
        return jsonify('You shouldn\'t do that')
    elif(len(blog_posts) > 25):
        return jsonify('Nice Try! But there\'s a limit')
    else:
        blog_posts.append({"title": title, "content": content})
        return render_template('index.html', posts=blog_posts)

@app.route('/revealMessage', methods=['POST'])
def reveal_message():
    secret = request.form.get('secret')
    if not secret or secret == 'secret code':
        hints = [
           'Interesting, you\'re sending empty data. This part of the page usually doesn\'t have much to offer.',
           'But since you\'re exploring quite a bit, have you taken a look at the guidelines that we have for automated explorers?',
        ]
        return jsonify(hints), 200
    else:
        return 'Try again!', 400

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory('./static', 'robots.txt')

@app.route('/hiddenFlag', methods=['POST','PATCH', 'PUT', 'OPTIONS'])
def hidden_flag():
    token = request.cookies.get('user_token')
    if not token or token not in user_progress:
        return 'Invalid token', 400

    if request.method == 'POST':
        return 'It\'s not going to be so easy! Delve deeper!'
    elif request.method == 'PUT' and not user_progress[token]["PUT"]:
        user_progress[token]["PUT"] = True
        return 'Right ahead!'
    elif request.method == 'PATCH' and not user_progress[token]["PATCH"]:
        user_progress[token]["PATCH"] = True
        return 'Right ahead!'
    elif request.method == 'OPTIONS' and not user_progress[token]["OPTIONS"]:
        user_progress[token]["OPTIONS"] = True
        return 'Right ahead!'

    if all(user_progress[token].values()):
        return 'OASIS{congratulations_you_found_the_hidden_flag}'
    else:
        return f'You\'re on the right path, keep going'

if __name__ == '__main__':
    app.run(port=3000)
