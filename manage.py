from app import app

def main():
    try:
        app.run(debug=True, host= '0.0.0.0',  port= 8080)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()