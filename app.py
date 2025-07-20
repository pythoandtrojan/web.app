from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_malware', methods=['GET', 'POST'])
def create_malware():
    if request.method == 'POST':
        malware_type = request.form['malware_type']
        target_os = request.form['target_os']
        output_file = request.form['output_file']
        tunnel = request.form.get('tunnel')
        mask = request.form.get('mask')
        port = request.form['port']
        connection_type = request.form['connection_type']

        # Comando para gerar o malware
        command = f"python generate_malware.py --type {malware_type} --os {target_os} --output {output_file} --tunnel {tunnel} --mask {mask} --port {port} --connection {connection_type}"

        # Executar o comando
        subprocess.run(command, shell=True)

        return send_file(output_file, as_attachment=True)

    return render_template('create_malware.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return redirect(url_for('admin_panel'))
        else:
            return render_template('admin_panel.php', error='Credenciais inválidas')
    return render_template('admin_panel.php')

@app.route('/admin_panel')
def admin_panel():
    return render_template('admin_panel.php')

if __name__ == '__main__':
    app.run(debug=True)
