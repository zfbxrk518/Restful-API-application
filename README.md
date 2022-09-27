# Restful-API-application

This is my homework2 form SK. He asked me to make a build a Restful API application with three requirements:
1. Use user register api endpoint
2. Use login api endpoint(JWT), return JWT
3. User data will be stored in a json file.
4. Use flask for the backend.

My blueprint:
Build a movie library website.This is a personal website for users to record their movies watched or not.For the homepage, contains the login, logout,forgot and reset password functions. When users log in, they can add, update and  delete the movie.

Tech:
Typerscript, Vue, Bootstrap, Flask

Install Vue:
sudo npm install -g @vue/cli
vue create appname
cd appname
npm run serve


Notes:
1.SPA: single page application
2. Exit from nano, confirm the name of the file and then press return button.
3. Run the a.py file in terminal: python3 a.py
4. Install the package in mac by using the normal way but showing an error "The operation was rejected by your operating system." Just need to add "sudo" in front of the command.
5. Change package.json "scripts" "serve": "vue-cli-service serve --port 3000" so the frontend start at 3000. Default port is 8080.


Frontend and Backend:
1. Frontend local: localhost:3000,
   Backend local: 127.0.0.1:5000 (localhost:5000)
2. Run frontend: npm run serve
   Run backend: . venv/bin/activate
                python3 main.py
