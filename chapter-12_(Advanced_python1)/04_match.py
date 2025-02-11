def status(status):
    match status:
        case 200:
            return "ok"
        case 300:
            return "oky oky"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(status(500))