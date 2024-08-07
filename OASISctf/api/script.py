from flask import Flask, request, render_template, jsonify, send_from_directory, abort, make_response
import uuid
import json
import base91

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

# Let's assume this is your database of blog posts
blog_posts = [
    {"title": "First Post", "content": "This is the first post."},
    {"title": "Second Post", "content": "This is the second post."},
    # Add more posts as needed...
]

def save_state_to_cookie(response, token, user_progress):
    state = {
        "token": token,
        "user_progress": user_progress
    }
    encoded_state = base91.encode(json.dumps(state).encode('utf-8'))
    response.set_cookie('state', encoded_state)

def load_state_from_cookie():
    encoded_state = request.cookies.get('state')
    if encoded_state:
        state = json.loads(base91.decode(encoded_state).decode('utf-8'))
        return state.get('token'), state.get('user_progress')
    return None, None

@app.route('/')
def home():
    token, user_progress = load_state_from_cookie()
    if not token:
        token = str(uuid.uuid4())
        user_progress = {"PATCH": False, "PUT": False, "TRACE": False}
        response = make_response(render_template('index.html', posts=blog_posts))
        save_state_to_cookie(response, token, user_progress)
        return response
    elif token not in user_progress:
        user_progress = {"PATCH": False, "PUT": False, "TRACE": False}
    
    response = make_response(render_template('index.html', posts=blog_posts))
    save_state_to_cookie(response, token, user_progress)
    return response

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
        response = make_response(render_template('index.html', posts=blog_posts))
        token, user_progress = load_state_from_cookie()
        save_state_to_cookie(response, token, user_progress)
        return response

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

@app.route('/hiddenFlag', methods=['POST','PATCH', 'PUT', 'TRACE'])
def hidden_flag():
    token, user_progress = load_state_from_cookie()
    if not token or not user_progress:
        return 'Invalid token', 400

    if request.method == 'POST':
        return 'It\'s not going to be so easy! Delve deeper!'
    elif request.method == 'PUT' and not user_progress["PUT"]:
        user_progress["PUT"] = True
        response = make_response('Right ahead!')
        save_state_to_cookie(response, token, user_progress)
        return response
    elif request.method == 'PATCH' and not user_progress["PATCH"]:
        user_progress["PATCH"] = True
        response = make_response('Right ahead!')
        save_state_to_cookie(response, token, user_progress)
        return response
    elif request.method == 'TRACE' and not user_progress["TRACE"]:
        user_progress["TRACE"] = True
        response = make_response('Right ahead!')
        save_state_to_cookie(response, token, user_progress)
        return response

    if all(user_progress.values()):
        return 'OASIS{congratulations_you_found_the_hidden_flag}'
    else:
        response = make_response('You\'re on the right path, keep going')
        save_state_to_cookie(response, token, user_progress)
        return response

if __name__ == '__main__':
    app.run(port=3000)
