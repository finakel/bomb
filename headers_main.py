import fake_useragent

headers_dnipro = {
        "User-Agent": fake_useragent.UserAgent().random,
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://dnipro-m.ua",
        "Referer": "https://dnipro-m.ua/ru/?campaignid=19338826483&adgroupid=145021258255&targetid=kwd-321958277646&adid=642262423899&network=g&keyword=%D0%B4%D0%BD%D0%B8%D0%BF%D0%A0%D0%9C&gad_source=1&gclid=CjwKCAiAm-67BhBlEiwAEVftNs6mIVIEnRvDbgR8I5H2r54Rb5aEezA3nuzhGbSv2VDLQEyaUa1C2xoC_f0QAvD_BwE",
        "X-Requested-With": "XMLHttpRequest",
        "x-csrf-token": "KMUvjCcvz7LJWQ7ikt4GYWqhvA6yQs0KX1Ck6EKJ2YVJmmjlCnC9y_4aZ9fzqnUyK9LRVIoG9EAxEd2Ac96t4w=="
    }
    
cookies_dnipro = {
        "session_hash": "8194cc9fe3261cc433267a12d738eb11",
        "language": "1f1c77ed088a525c9d9a3ee0075b68d6a50c75278eb07b95c9c6c8adf4633886a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22language%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D",
        "ab_1": "2",
        "translations_pushed": "92f83c1f3a434aeae744854c974cdb236df315cbe39e518ed7234b1ea9a0cd88a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22translations_pushed%22%3Bi%3A1%3Bi%3A1%3B%7D",
        "sc": "A0572E88-05B8-1FEF-D02A-2342A1BFAC2E",
        "_gcl_au": "1.1.1479450579.1735577460",
        "_ga_4JZL75V9F8": "GS1.1.1736175252.2.1.1736175270.42.0.0",
        "_ga": "GA1.1.389738311.1735577460",
        "_ms": "0f0069e1-847b-4d99-894a-792…i%3A1%3BN%3B%7D",
        "gclid": "939156d81035356c746423ecca0a2cf4a2748f879bd3dc65cfa6250fb7064ccea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22gclid%22%3Bi%3A1%3Bs%3A8%3A%22dnipro-m%22%3B%7D",
        "_csrf-frontend": "abfe683ee8f7d6733b28c5574a3d7e5de5e9df985472b96e1d826553725fbbeda%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22a_Gi-_ry7Ci5atsSAsmZ8D9JnAyh1Wtf%22%3B%7D",
    }
    
headers_citrus = {
            "User-Agent": fake_useragent.UserAgent().random,
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=utf-8",
            "Content-Length": "75",
            "Origin": "https://www.ctrs.com.ua",
            "Referer": "https://www.ctrs.com.ua/actions/new-year/?gad_source=1&gclid=CjwKCAiAm-67BhBlEiwAEVftNrXay4Ki2DUK52X0X7kukhFV0Eizbq0Ae7TVYo74G4k4g6yTF_pAzxoCH2gQAvD_BwE",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "TE": "trailers",
            "X-App-Token": "yF27jwg5orUVo4abrops",
            "x-locale": "uk"
        }
    
cookies_citrus = {
            "deduplication_cookie": "CjwKCAiAm-67BhBlEiwAEVftNrXay4Ki2DUK52X0X7kukhFV0Eizbq0Ae7TVYo74G4k4g6yTF_pAzxoCH2gQAvD_BwE",
            "_gcl_aw": "GCL.1736176857.CjwKCAiAm-67BhBlEiwAEVftNrXay4Ki2DUK52X0X7kukhFV0Eizbq0Ae7TVYo74G4k4g6yTF_pAzxoCH2gQAvD_BwE",
            "_gcl_gs": "2.1.k1$i1736176834$u8975591",
            "_gcl_au": "1.1.1653348159.1736110246",
            "sc": "2A937DB6-A15F-B517-3A25-88E94C1CF547",
            "_ga_LNJDP61TWH": "GS1.1.1736176857.2.0.1736176857.60.0.334077109",
            "_ga": "GA1.1.566819935.1736110247",
            "_ttgclid": "CjwKCAiAm-67BhBlEiwAEVftNrXay4Ki2DUK52X0X7kukhFV0Eizbq0Ae7TVYo74G4k4g6yTF_pAzxoCH2gQAvD_BwE",
            "_fbp": "fb.2.1736110248200.517121377217213606",
            "_clck": "1qvy6am%7C2%7Cfsc%7C0%7C1831",
            "_clsk": "newjjm%7C1736176861420%7C1%7C1%7Ci.clarity.ms%2Fcollect"
        }

headers_easypay = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "AppId": "0f18d21c-5144-4a71-8da3-d32acc8fe661",
        "Content-Type": "application/json; charset=UTF-8",
        "GoogleClientId": "GA1.2.1076156160.1736110122",
        "GoogleSessionId": "1736241333",
        "Host": "auth.easypay.ua",
        "locale": "ua",
        "Origin": "https://easypay.ua",
        "PageId": "7dc9f791-0cbe-4268-ad25-e969799cfc36",
        "PartnerKey": "easypay-v2",
        "Referer": "https://easypay.ua/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers",
        "User-Agent": fake_useragent.UserAgent().random,
        "Connection": "keep-alive"
    }

headers_uvape = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Length": "121",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "uvape.pro",
    "Origin": "https://uvape.pro",
    "Referer": "https://uvape.pro/ua/pod/pod-systemy-vaporesso",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "User-Agent": fake_useragent.UserAgent().random,
    "X-Requested-With": "XMLHttpRequest",
}

cookies_uvape = {
    "_ua_redirect_": "ua",
    "PHPSESSID": "d637d4638ed59d7b0b8fcf4021868101",
    "currency": "UAH",
    "default": "d637d4638ed59d7b0b8fcf4021868101",
    "geoip_confirm": "1",
    "prodex24cur_domain": "uvape.pro",
    "prodex24source_full": "https://www.google.com/",
    "prodex24source": "google.com",
    "prodex24medium": "organic",
    "prodex24campaign": "",
    "prodex24content": "",
    "prodex24term": "",
    "language": "uk-ua",
    "li_nr": "1",
    "_ga_WFCSSHEKNY": "GS1.1.1736335958.1.1.1736335971.47.0.0",
    "_ga": "GA1.1.68086763.1736335958",
    "_clck": "1vvp31s|2|fse|0|1834",
    "TELERSESSION_REFERRER": "https://www.google.com/",
    "_clsk": "1pjoez9|1736335959690|1|1|z.clarity.ms/collect",
    "hideModal": "true",
}

headers_terravape = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Length": "179",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "terra-vape.com.ua",
    "Origin": "https://terra-vape.com.ua",
    "Referer": "https://terra-vape.com.ua/ru",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "User-Agent": fake_useragent.UserAgent().random,
    "X-Requested-With": "XMLHttpRequest"
}

cookies_terravape = {
    "OCSESSID": "196d914cee4c670371768227e3",
    "_ga": "GA1.1.8431661.1736337994",
    "_ga_EMQZQWEWLV": "GS1.1.1736337993.1.1.1736338016.0.0.0",
    "currency": "UAH",
    "language": "ru-ru",
    "prodex24cur_domain": "terra-vape.com.ua",
    "prodex24source_full": "https://www.google.com/",
    "prodex24source": "google.com",
    "prodex24medium": "organic",
    "prodex24campaign": "",
    "prodex24content": "",
    "prodex24term": ""
}

headers_moyo = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Form-Data": "251b2615b913e59efbd8165f4530a630",
    "Content-Length": "84",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": fake_useragent.UserAgent().random,
    "Origin": "https://www.moyo.ua",
    "Referer": "https://www.moyo.ua/ua/promo/promo2024/?utm_source=google&utm_medium=cpc&utm_id=19191373185&utm_campaign=Performance_Max_%D0%91%D0%A2_Shopping_ru&gad_source=1&gclid=Cj0KCQiA4fi7BhC5ARIsAEV1YiYsNu8VQS-ks4MT1PiHpRdDcoAB4DRfQoW4FMulALaCq5FBa63i0LEaAhPAEALw_wcB",
    "TE": "trailers",
    "Host": "www.moyo.ua",
}

cookies_moyo = {
    "lang": "uk_UA",
    "basket": "0b5a74903c9940e3c73282ca8195910f",
    "basket_summary_products": "0",
    "basket_summary_money": "0",
    "_gcl_aw": "GCL.1736358405.Cj0KCQiA4fi7BhC5ARIsAEV1YiYsNu8VQS-ks4MT1PiHpRdDcoAB4DRfQoW4FMulALaCq5FBa63i0LEaAhPAEALw_wcB",
    "_gcl_gs": "2.1.k1$i1736358399$u182813242",
    "_gcl_au": "1.1.7857585.1735412933",
    "source": "sourceCookie|utm_source",
    "utm_source": "google",
    "sc": "F04B174B-7EC8-DFA8-06F3-2966B1587034",
    "__user_id": "uid-1637194752.2542748805",
    "biatv-cookie": '{"firstVisitAt":1735412934,"visitsCount":3,"currentVisitStartedAt":1736352409,"currentVisitLandingPage":"https://www.moyo.ua/ua/promo/promo2024","currentVisitUpdatedAt":1736358404,"currentVisitOpenPages":3}',
    "YII_CSRF_TOKEN": "bGhHMjg2MkZOdm5NMXFKWmd4YzE3WjdHTXdWRm1TcTBKga2o0eJgnVgvLWnrZgtJtUam2KS3Z8M4n40tWGYkcw==",
    "init_source_page": "https://www.moyo.ua/ua/promo/promo2024",
    "isContextQuery": "1",
    "new_user_ga": "1",
    "no_detected_user_ga": "0",
    "__utmb": "46025016.1.10.1736358406",
    "__utmc": "46025016",
    "__utmt_UA-16250353-8": "1",
    "_hjSession_2660990": '{"id":"99c53df2-8a10-491a-9a2c-3f12ff808cee","c":1736358406148}',
    "_dc_gtm_UA-16250353-2": "1",
}

headers_sushiya = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Authorization": "Bearer demo",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "sushiya.ua",
    "Origin": "https://sushiya.ua",
    "Referer": "https://sushiya.ua/ru/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": fake_useragent.UserAgent().random,
    "Cookie": (
        "dae23e1f6b5bf8609e2224d695520311=ru-RU; affclick=; _ga_1H1QWKT0HX=GS1.1.1736422359.3.0.1736422359.60.0.0; "
        "_ga=GA1.2.124348765.1735422421; _ga_VMMXEZPH1B=GS1.2.1736422361.3.0.1736422361.0.0.0; "
        "_fbp=fb.1.1735422426358.237273888579184282; popup_sushiya=61d015a3d466d1119c01095c4960ab10; "
        "5c56ddacb7d52afbab2130776ac59994=hcub0b63rumponpmi55pm84o8g; _gid=GA1.2.1487604020.1736422361; "
        "_gat_gtag_UA_155856_12=1; _gat=1"
    )
}

headers_zolota = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "zolotakraina.ua",
        "Origin": "https://zolotakraina.ua",
        "Referer": "https://zolotakraina.ua/ua/kolca/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "X-Requested-With": "XMLHttpRequest",
    }

cookies_zolota = {
    "form_key": "PKRxVkPlQqBlb8Wi",
    "PHPSESSID": "e93e5fc65beb3d411dd45e07153a1ee8",
    "private_content_version": "ee89cd8fd143ee7bb469f947a70742b0",
}

headers_avtoria = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "auto.ria.com",
    "Origin": "https://auto.ria.com",
    "Referer": "https://auto.ria.com/iframe-ria-login/registration/2/4",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": fake_useragent.UserAgent().random,
}

cookies_avtoria = {
    "chk": "1",
    "_gcl_au": "1.1.1378799276.1736678691",
    "_ga_KGL740D7XD": "GS1.1.1736678690.1.1.1736678694.56.0.422786723",
    "_ga": "GA1.1.1886750303.1736678691",
    "test_new_features": "337",
    "ab-link-video-stories": "2",
    "news_prior": "%7B%22item0%22%3A5%2C%22item1%22%3A4%2C%22item2%22%3A3%2C%22item3%22%3A2%7D",
    "test_fast_search": "1",
    "_504c2": "http://10.42.11.33:3000",
    "PHPLOGINSESSID": "sbpni99dl4p0176fr6e2uib1m2",
    "project_id": "2",
    "project_base_url": "https://auto.ria.com/iframe-ria-login",
    "ui": "c9fd53eb2cc083c4",
    "__utma": "79960839.1886750303.1736678691.1736678696.1736678696.1",
    "__utmc": "79960839",
    "__utmz": "79960839.1736678696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "__utmt": "1",
    "_gat": "1",
    "showNewFeatures": "7",
    "PHPSESSID": "eyJ3ZWJTZXNzaW9uQXZhaWxhYmxlIjp0cnVlLCJ3ZWJQZXJzb25JZCI6MCwid2ViQ2xpZW50SWQiOjMzODg4MjI1MDcsIndlYkNsaWVudENvZGUiOjc1MDgxNDE0OCwid2ViQ2xpZW50Q29va2llIjoiYzlmZDUzZWIyY2MwODNjNCIsIl9leHBpcmUiOjE3MzY3NjUwOTU4NzMsIl9tYXhBZ2UiOjg2NDAwMDAwfQ==",
    "_ga_MHN7ZGH3LY": "GS1.1.1736678696.1.1.1736678731.0.0.0",
    "_gid": "GA1.2.1223636075.1736678697",
    "_clck": "1iollo6%7C2%7Cfsi%7C0%7C1838",
    "_clsk": "1423o84%7C1736678702475%7C2%7C1%7Co.clarity.ms%2Fcollect",
    "gdpr": "[2,3]"
}
