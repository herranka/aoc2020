def dl(fname, day, year):
    import requests
    from secret import session
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', session)
    url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    r = requests.get(url, cookies=jar)
    if 'Puzzle inputs' in r.text:
        print('Session cookie expired?')
        return r.text
    if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
        print('Output not available yet')
        return r.text
    if r.status_code != 200:
        print('Not 200 as status code')
        return r.text
    with open(fname,'w') as f:
        f.write(r.text)
    return 0

if __name__ == "__main__":
    import sys
    from fetch import dl
    year = 2020
    fname = "in"
    dl(fname, sys.argv[1], year)