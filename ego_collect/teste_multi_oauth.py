# -*- coding: latin1 -*-
#
################################################################################################
# Script para testar autenticação com múltiplas contas:	
#

import tweepy

##############################################################################################################
#####consumer_key="ffap5ENG3yu0u7phgdhQzIvJx"
#####consumer_secret="bFXgZjBUGMRoSfxbKLNZG8Y0IqjUPoc9O4vgKOtUCs0WSlkT6s"
#####access_token="813458922967302144-f3aEkz6OsueSD6eCkaN1yYXVcYXPGuZ"
#####access_token_secret="OG08x1kx6rgMHwwEcmQKeeEAot88UALSQAY96XlGnpRba"
#####
#####
#####consumer_key="L8LX4gmyLYpfaUDHPRTmAnO5E"
#####consumer_secret="pCte0UiHaPIBbReSTTFm3pGV8mlS9L7b28azjIZ8vr7Sv320m4" 
#####access_token="813458922967302144-wgByKpL2mDieJRbLrMbKxDySesoSHSS"
#####access_token_secret="i81wWiwi6MWNUgg8CHz5Z0S9zTUWSq3cSvmy44nBCKPE6"
#####
#####consumer_key="O4t25YPnHGNm7B1i5qaN7Gu3s"
#####consumer_secret="v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR"
#####access_token="813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi"
#####access_token_secret="VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB"
#####
#####consumer_key="R5iaxJ4FpLL6pcDOrr2osLNKr"
#####consumer_secret="PRNJxduOZgGsmjDlIeZIMuPF8qaauSxzYDlggdLWb1S3A5AOXO"
#####access_token="813460676475842560-2aJSRKgnhugK16w1T4AERo0pkoNtjxO"
#####access_token_secret="pSUfiFZmyb68U4YihPMFKWSQYKk2Js4cqGEgKNVbeS5xk"
#####
#####consumer_key="w9GvsiaQy9jcBDTKIaXomBjQT"
#####consumer_secret="H53rMVNGlrUvYFnN5f5ud1JzrGkhVpz2e335KBK413KrEK8Mwc"
#####access_token="813460676475842560-moOTo31XN8tbUbrKM3QOitihXsPD1Z9"
#####access_token_secret="aGuidWdVzC24kkUSJ6BNDxKRwUPchCz0LWtEnVINJShY3"
#############################################################################################################
#consumer_key="JeSUTJXGauV6RY7i6RJDSRvoL"
#consumer_secret="ZCOMtPUTAJPFuEwm8S50wPIGF0CpVVFRJIQauy1DcSZ4w6v6ox"
#access_token="41112432-fRQMmcN5D6mSgg8kPy9oNZqDRSujUkCjAQcPgwHOb"
#access_token_secret="FxU83OnYRfr6eU8IWuj5pP2SviFsyu2UHAaGMJqjyD6a4"
#
#
#consumer_key="BVtFIlaU1Rs8jMKezdokGm3jw"
#consumer_secret="GsuNXNb3LquS3B0mvPP7P7SwmQAbwsdBtnW1ly6xx1mAuh6Skd"
#access_token="41112432-GEjhDhnskU3YQirkhQEiAsjHlHOtorBgTjNVZXX71"
#access_token_secret="JauW55aDctyQh4UGBTf2LN9VlIELJWufFitxFuHCIyG69"
#
#consumer_key="qvmfyEldFvEmTCAvzFSBTP1wz"
#consumer_secret="L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA"
#access_token="786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0"
#access_token_secret="in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ"
#
#
#consumer_key="pPHJxZodM0fJcqO6rNOpgSuKX"
#consumer_secret="PDJBEaHi0A255Ku5P1fHJzLkwgzWNZdFrAdoNRtjtxuYnuquu3"
#access_token="786664983862083584-0DPtb9gb0L0V86AahLzsVCX7maUWU48"
#access_token_secret="CQATIM33fPHoq9uEVXVbkixdOmJnotkntLAHzpqLUGRw8"
#
#
#consumer_key="VMkcoyd5vate9jLbW0ze6yp0a"
#consumer_secret="XsDwoTCE2AhiXeRyNu38XhcxZChE44kl9ED10U5BA9vzKWFUpE"
#access_token="786664983862083584-Zii8faTHCNUSLv9SjYNasYZfUFIMkZy"
#access_token_secret="TFMiyIQfTv25M1UXdV8XUHO8La3Pk0F9BI2og8qAVPBhs"
#
#
#consumer_key="UNwhnaGwIzjeNIb9p796O4cBl"
#consumer_secret="XkyvDXE9AiFdgd6bjiyeyvxgqgitIgsdRrRAZbcfGx74GHOWsN"
#access_token="786664983862083584-BcES2YdF1jjCl7Hg2vumGfPidwyxZTT"
#access_token_secret="iPkexY0o16DejWq5MfGs8uR6UeloY8koblw3cOVVP1FC6"
#
#consumer_key="U7NBO7duqO1aTZ81q63Hy61Er"
#consumer_secret="kVKISoiaUrw1gBAZpTLPJ1op8GfONmHULeTMG01Ofj2OsAMkOg"
#access_token="781627388329398273-lrXG081wRlkvHpYAPO0iS77p3fGnijs"
#access_token_secret="cR71hKrAb4zZIyZqGIwDuH0HMnC1Z7BAwN7MKEfe7Uhg7"
#
#
#consumer_key="k2X1NYSSfLxqbTElsaJoamTpA"
#consumer_secret="ywBx5cyqHmKrFtziklEgtzAJKHTtz5ORXAFNvdEcIyyv6KH9uc"
#access_token="781627388329398273-CkaxgovlocA4s2OVJdyyBwZh495uIZM"
#access_token_secret="i0zSthAta9HIH6dNTSlVrLQnrsBt1fVM2cjpFQIpFmBx0"
#
#consumer_key="4MuJwZbOxwNIMFGYlbxGp7dfO"
#consumer_secret="pz9s4lUAFJm8y1ikEbHyPkgB1cFVg3jZiDV94TIwqpJ8hx34mD"
#access_token="781627388329398273-VrkEYPxLhJp7wbv0rbVXuo3RxPqz5Wi"
#access_token_secret="den2GRsGzlVng6l9TWcXGjE7pWhmXX7UHK2qauzqZyPwF"


oauth_keys={'consumer_key':["ffap5ENG3yu0u7phgdhQzIvJx","ffap5ENG3yu0u7phgdhQzIvJx","L8LX4gmyLYpfaUDHPRTmAnO5E","O4t25YPnHGNm7B1i5qaN7Gu3s","R5iaxJ4FpLL6pcDOrr2osLNKr","w9GvsiaQy9jcBDTKIaXomBjQT"],
				'consumer_secret':["bFXgZjBUGMRoSfxbKLNZG8Y0IqjUPoc9O4vgKOtUCs0WSlkT6s","pCte0UiHaPIBbReSTTFm3pGV8mlS9L7b28azjIZ8vr7Sv320m4","v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR","PRNJxduOZgGsmjDlIeZIMuPF8qaauSxzYDlggdLWb1S3A5AOXO","H53rMVNGlrUvYFnN5f5ud1JzrGkhVpz2e335KBK413KrEK8Mwc"],
				'access_token':["813458922967302144-f3aEkz6OsueSD6eCkaN1yYXVcYXPGuZ","813458922967302144-wgByKpL2mDieJRbLrMbKxDySesoSHSS","813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi","813460676475842560-2aJSRKgnhugK16w1T4AERo0pkoNtjxO","813460676475842560-moOTo31XN8tbUbrKM3QOitihXsPD1Z9"],
				'access_token_secret':["OG08x1kx6rgMHwwEcmQKeeEAot88UALSQAY96XlGnpRba","i81wWiwi6MWNUgg8CHz5Z0S9zTUWSq3cSvmy44nBCKPE6","VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB","pSUfiFZmyb68U4YihPMFKWSQYKk2Js4cqGEgKNVbeS5xk","aGuidWdVzC24kkUSJ6BNDxKRwUPchCz0LWtEnVINJShY3"]}


# create authentication handlers given pre-existing keys  

auths = []

j=0
for i in oauth_keys:
	consumer_key = (oauth_keys['consumer_key'][j])
	consumer_secret = (oauth_keys['consumer_secret'][j])
	access_token = (oauth_keys['access_token'][j])
	access_token_secret = (oauth_keys['access_token_secret'][j])
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	
	auths.append(auth)
	j = j+1

print (auths)

api = tweepy.API(auths, wait_on_rate_limit=True)
