from requests import request

res = request("get", 'https://alist-replit.kkkaroth.repl.co/')
print(res.status_code)
