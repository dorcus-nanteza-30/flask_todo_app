from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1"},
    {"id": 2, "title": "Task 2"},
    {"id": 3, "title": "Task 3"}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    title = request.form.get('title')
    if title:
        new_task = {"id": len(tasks) + 1, "title": title}
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if request.method == 'POST':
        task['title'] = request.form.get('title')
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
