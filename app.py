from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)  #membuat objek Flask

#route untuk halaman utama (index)
@app.route('/')
def index():
    return render_template('index.html')  #halaman utama dengan link login

#route untuk halaman login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm', 'Guest')          #mengambil data nama dari form
        return redirect(url_for('success', name=user))  #mengalihkan ke halaman success dengan nama pengguna yang diambil dari form
    else:
        return render_template('login.html')            #mengalihkan ke halaman login

#route untuk halaman sukses
@app.route('/success/<name>')
def success(name):
   return render_template('success.html', name=name)    #mengalihkan ke halaman success dengan nama pengguna yang diambil dari form

#memulai aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)  #menjalankan aplikasi dalam mode debug agar lebih mudah menemukan kesalahan
