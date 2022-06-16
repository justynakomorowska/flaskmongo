from app import create_app, db

app = create_app()

@app.cli.command()
def deploy():
    print("deploying fresh")
    db.create_all()