import urllib

cur = "act=3&rub=1&rub_pub_save=1&topmenu=2&actions=1&f0=78.90.66.126&f1=1&f2=&f3=&f4=1&f7=2%7E&f28=&f29=&f43=&f44=&f30=EUR&f26=&f27=&f41=1&f31=&f32=&f38=%E3%F0%E0%E4+%D1%EE%F4%E8%FF&f42=&f39=&f40=%CC%E0%ED%E0%F1%F2%E8%F0%F1%EA%E8+%EB%E8%E2%E0%E4%E8%2B&fe3=&fe4=&f45=&f46=&f51=&f52=&f33=&f34=&f35=&f36=&f37=&fe2=1"


def do_it(data):
    params = data.split('&')
    res = ""
    for param in params:
        key, value = param.split('=')
        if not value.isdigit():
            value = '"{}"'.format(value)
        res += ('"{}": {}, '.format(key, value))
    print(res)

do_it(cur)

a = "f1%091%09slink%093ymjno%09act%093%09"
v = urllib.parse.unquote_plus(a).split('\t')
index = v.index('slink')
print(v[index + 1])