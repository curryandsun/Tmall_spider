url_ori_list = [
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-21980715049.46.39614a1fBDZEU5&id=601047720268&rn=77bc01ef815b0d419478993ac64a7ae7&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-21980715049.53.39614a1fBDZEU5&id=601279129466&rn=77bc01ef815b0d419478993ac64a7ae7&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-18584437813.94.68f7cc3cc9yDa6&id=559831104757&rn=7fe8bb360ae57c7420aff8145c0b8476&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-18584437813.101.68f7cc3cc9yDa6&id=601477648723&rn=7fe8bb360ae57c7420aff8145c0b8476&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16413478645.50.4007240dAneqZD&id=45129832334&rn=7b73ff96ebf984526d5a9f56a2386312&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16413478645.57.4007240dAneqZD&id=569856571465&rn=7b73ff96ebf984526d5a9f56a2386312&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22404261671.60.353b3360wviLMN&id=616923065231&rn=1b9ab360d22eff79884f234570964194&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22404261671.64.353b3360wviLMN&id=615376472179&rn=1b9ab360d22eff79884f234570964194&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-19013603916.86.3c8e42c4CjQN4o&id=594563626444&rn=2aa2d335a0de82deb5f166963705555d&abbucket=14',
    'https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-19013603916.91.3c8e42c4CjQN4o&id=526927286858&rn=2aa2d335a0de82deb5f166963705555d&abbucket=14'
]

url_comment_list = [
    'https://rate.tmall.com/list_detail_rate.htm?itemId=601047720268&spuId=1317382822&sellerId=2206435562633&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvA9v4vXgvUvCkvvvvvjiWP2cytj1bRsMhsjYHPmPwtjimP2LvsjnhP2SZljlb9vhvHHiaqUCzzHi47IKYt11R7Yr4%2BaGB9vhv2HifzO36zHi47IfYzs9Cvvpvvvvv9vhv2HiaKSYQzHi475dbzgvCvv147GRv5n147DiKpa%2F%2BvpvEvvBnkkyivhkmdvhvmpvhwvK8k9CvjuQCvvyvmv9b%2FM%2BvP80%2BvpvEvvkWklBZvC2X29hvCvvvMMGvvpvVvmvvvhCvmvhvLvsC9pvjRSexfwofdeQEfwLwaXgXaZmOD7zh58t%2Bm7zhtj7JPAx%2F1n1l%2Bb8rwZXlYExreEIaRtxr1RoKHkx%2F1RBlY2%2FAVAdwafmxdXkgvpvIvvvv2yCvvvvvvvhkphvUgpvv96CvpC29vvm2phCvhjvvvUnvphvpw89Cvv9vvUvqeGRDRO9CvvOUvvhCJhggvpvhvvvvv8OCvvpvvUmm39hvCvvhvvm%2BvpvEvv94kMsGvCmQdvhvmpvUyQKUkvvOU8QCvvyvmEgb0rIvVHR%2BvpvEvvQPmgKbv216dvhvmpvhJgus%2BQCUo8QCvvyvCRR8MN6voUZgvpvhvvvvv29Cvvpvvvvv&needFold=0&_ksTS=1609997785943_897&callback=jsonp898',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=601047720268&spuId=1317382822&sellerId=2206435562633&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvr9vcvcGvUvCkvvvvvjiWP2cytj1hnLzUAjivPmP9ljlPRFcU6jtRn2qyzjEb9vhvHHianOvgzHi475UKtMQ67lH4%2BaGBRvhvCvvvphm%2BvpvEvUj76TZvvvRCdvhvmpmC%2FP0ZvvmmVOOCvvpv9hCvRvhvCvvvphvvvpvVvvBvpvvvuvhvmvvvpLaS4BrbkvhvC9hvpy290b9Cvm9vvhCwvvvvvvvvpkIvvvhGvvCj1Qvvv3QvvhNjvvvm29vvBGwvvvURmvhvLUjWH3Oa3LIBHdBYBR2hV1OqrADn9Wma%2BfmtEpcUT2eARdIAcUmxdXuK5FXXiXhpVC4AVAYlYb8reTt%2Bm7zwdiTAdcvr%2BE7rV8TJR6ORvpvhvv2MMTOCvvpvvhHhdvhvhIoCrfjevvmvIqhSpqoxP2It%2B8QCvvyvvyBvXQvv9Pu%2BvpvEvUVZyc9vvvV1dvhvmpmCMP5vvvvCOTQCvvyv9JzIVpvv9KJ%2BvpvEvUhkETOvvvWadvhvmpvCi4ngvvv2rTQCvvyvv4%2FiUvvvvY7vvpvW7DgpURPw7Di4XOPNRvhvCvvvphv%3D&needFold=0&_ksTS=1609997897643_1050&callback=jsonp1051',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=559831104757&spuId=889688217&sellerId=3430935233&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hv59vXvXOvUvCkvvvvvjiWP2cytj1HRFz9Aj3mPmPy0jtWP2cwsjn8RsqWAjlbRvhvCvvvvvvgvpvhvvvvvUvCvv147%2FIOkr147DiKUa%2F%2BvpvEvvpYCm%2BdvmmpdvhvmpvhLpp3UpvwguQCvvyvCVvhJj9vjR0%2BvpvEvvkCvi0avC2A39hvCvvhvvmevpvhvvmv9d9Cvm9vvvvRphvvvvvvvLBvpvF3vvm2phCvhRvvvUnvphvpwvvv96CvpCCQkvhvC99vvpHgLu9Cvv9vvUvqeGviNp9CvhQW8pUvCsMv6WmQRqwiLO2vqU0QKoZH1nsIAfUTnZJt9ExreEyanuAQiNofVcCv%2BneYiLUpwhKn3w0xhE3gp%2Bex6aZtn0vHfJBlYb8rvvhvC9v9vvCvpvgCvvpvvPMMRvhvCvvvvvm%2BvpvBUv9R9Oohvv3U84GuUZWE3we%2BvpvEvv9U9uTKvCBldvhvmpvUk9nZxvvZeTQCvvyvCPO26rUvVbm%2BvpvEvvBi9lCpvCkLdvhvmpvh5Qplnpv99OvCvv14c9I9Ea147Dil9aGgvpvhvvvvvUvCvCB4cXAv0Y147DuvSKwwNlAL7djNhp%3D%3D&needFold=0&_ksTS=1609997971861_849&callback=jsonp850',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=601477648723&spuId=1325204784&sellerId=3430935233&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvLvvavaOvUpCkvvvvvjiWP2cytj1HnLcvljljPmPWtjl8nLsw1j1WRsswQjiRRIvCvCLwPREQ9aMwznAhNxSStaQczWX49OvCvvswPPrJArMwzns3rxuvvpvWz2s%2F4ZzNznswjDC4RvhvCvvvvvmvvpvWz2sk4dqNznswNfn4dvhvmpvWR9wR29vyTTQCvvyv2bAV0n9vEjvgvpvhvvvvv8QCvvyvCnkVh3UvHCk%2BvpvEvv9u3wP2vvAK39hvCvvhvvvUvpCWmnfBvvaw0jc6LLIt8ZJaKE5ErqO24gcE2f6A%2Be9nfaCliC4AVA1lYExreTtd2ezOafm655H2gWLy%2B2Kz8Z0vQRAn%2BbyDCaFIAXZTKd9Cvm9vvvvRphvvvvvv9pCvpvF3vvm2phCvhRvvvUnvphvpwvvv96CvpCCQuvhvmvvv92KfQVYjkvhvC99vvpHgL9vCvvOvUvvvphvRvpvhvvvvv29Cvvpvvvvvi9hvCvvv9U8%2BvpvEvv9UCKLyvCvXdvhvmpvhwQ4%2FS9vprIvCvvswMPD5GYMwznAwADu%2BvpvEvv15336avmvCdvhvmpvWLIX3Opv9HuQCvvyv2WVjQWvv8RV%2BvpvEvv1HmRs%2BvmQfRvhvCvvvvvmvvpvWzC1aaPPNznswvnx49vhvHnQGzjCEzYswz8bF7%2FMDzCNw1DuC&needFold=0&_ksTS=1609998016835_606&callback=jsonp607',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=45129832334&spuId=331529701&sellerId=2455148177&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvKvvXvOgvUpCkvvvvvjiWP2cytjn2RFcwzjthPmPvljtERsMwtj3EP2q9Ajr2PF9CvvBvpvvvRvhvChCvvvmvvpvWzHAb4BPNznswNS34dvhvmZC2JkQPvhCWL8QCvvDvp0w%2ByQCvogygvpvhphvvv8QCvvDvpXWIEvCvoxk%2BvpvEphHzUEQvphaudvhvmZCmmkvVvhCV5TQCvvDvpBwwTQCvprk%2BvpvEphjKjj6vphE0dvhvmZCCb31lvhCCiIOCvvBvppvvi9hvChCvCCpgvpvhphvvvb9Cvm3vpvCQvvCvphCvC2WvvhUTphvwv9vvBj1vpCQmvvCh7hCvjvUvvhBOkvhvCyEmmv9wVT9Cvv3vpvLXqoTQIv9Cvh1COwhvIshw4cCmAWQKK5Cmwyn1lB9XahZw4w2UeX9w4cCmQWQKK5CmahE1lB9XwBUw4w2UV39w4cCmQUZKK5CmwZX1lB9Xwhpw4w2UvvhvCyCUvvvvvvgCvvpvvvvvdvhvmZCCrApuvhCUnuQCvvDvpBU%2BVQCvoLAvvpvWzPsJXcjNznswjBx49vhvHnQGhVg8zYswzVC%2B7%2FacjPqw1DuC&needFold=0&_ksTS=1609998079113_2186&callback=jsonp2187',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=569856571465&spuId=973574139&sellerId=2455148177&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvmvv4v4OvUvCkvvvvvjiWP2cytjnmPFLhgjrCPmPO6jtERsdptjlERssOtjn89vhvHHiaHj2KzHi475fItM1f7Ma4%2BaGBRvhvCvvvvvmvvpvW7D%2BuJUcw7Di443fNRvhvCvvvvvm%2BvpvEvvLz9F6YvCAvdvhvmpvhSUUOVvvOp8QCvvyvCWUH9Ohv2VAVvpvhvvpvv8OCvvpvvUmmRvhvCvvvvvvRvpvhvv2MMQ9CvhQhs5gvCsNwTR2hjE1%2BVd0DyOvO5onmsX7v1CIaWDNBlwethbUf8zc6D70fdeQEfa1lYb8rwm0QD7zhdigDN%2BBldE7re161D7zvaXgqkvhvC99vvpHgLu9Cvv9vvUvqeGXLlb9Cvm9vvvvRphvvvvvvvatvpvF3vvm2phCvhRvvvUnvphvpwvvv96CvpCCQvvhvC9v9vvCvp8QCvvyvC20h6rUvmm7%2BvpvEvvpqCfetvvQudvhvmpvhE9ZznQvWPTQCvvyvCmGHOeUvhhm%2BvpvEvvotCZ3UvCmXdvhvmpvhnOoDipvp%2FIvCvCB47MU9nr147DiN%2F%2FNGvHi%2B7rPNp29Cvvpvvvvvdvhvmpvh0UU5EQvOaOvCvv14cU6vYr147DiDynG%3D&needFold=0&_ksTS=1609998135476_2211&callback=jsonp2212',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=616923065231&spuId=1624788190&sellerId=2207268032205&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hv19v4vXgvUvCkvvvvvjiWP2cytjnmnL5UzjD2PmPWgj18RLs9tjnjR2sWQj3bRvhvChCvvvmvvpvW7D1SwmNw7Di44T2NdvhvmZC24ZFfvhCRUuQCvvDvpQiUgvCvLyK%2BvpvEphRkoRWvphzSRvhvChCvvvm%2BvpvEphPkVhOvphZudvhvmZC2Y334vhChu8QCvvDvpT9wOvCvpYe%2BvpvEphPvVVgvphbU39hvChCCvvmUvpvVpyUUmCQfuvhvmhCvCn5rbtdpKvhv8hCvvjvvvhCvphvUY9vvpFivpCQmvvChNhCvjvUvvhBOphvwv9vvBH9UvpCWpWEiv8WOjoC3ZfmD5i3QpcCj%2BnezrmphwhKn3feAOH3TmEcBKFyK2kyZD76Od5QXVAdpaBw0EZ%2B5ZTjGeE3lBzxP1WA4ec3ZnDeDypvCvvXvovvvvvvRvpvhvv2MMs9CvvBvpvvvi9hvChCvCCovvpvW7DSdhvPw7Di47rsNRvhvChCvvvm%2BvpvEphPIjUpvphEadvhvmZC2v31PvhCh7TQCvvDvpMOOJvCvBWVvvpvW7D0Hmhsw7Di4OB5N9vhvHHiaj7F%2BzHi47IB1t1AN7Yl4%2BaGB&needFold=0&_ksTS=1609998206152_612&callback=jsonp613',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=615376472179&spuId=1598678756&sellerId=2207268032205&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvYvvXvXwvUpCkvvvvvjiWP2cytjnCRsqZljYHPmPU1jr2PLShgjrWn25yljiERL9CvvpvvhCv9vhv2nsG%2B000zYswz2gT7IvCvvswjCENYaMwznsaZDu%2BvpvEvUm8FQUvvUHAdvhvmpmvqR92vvvCMpgCvvpvvvvvvvhvC9vhphvvvb9Cvm9vvhCwvvvvvvvvpSGvvvhGvvCj1Qvvv3QvvhNjvvvm29vvBGwvvvURkvhvC9hvpy29089Cvv9vvhhzfghhDp9CvhQvrZtRjX7reCAKX9nr1CKKHdUf8aBl5F%2FAdcE2afmAdBeOjomxfBe4d3WDN%2BLOd34AdcEjaNpM%2Bu6XwoAQD46Xe8tYVVzhj8gL%2B3%2BuRvhvCvvvphmevpvhvvCCBUOCvvpv9hCvdvhvmpvvSddXvvvvq4QCvC8h9v9Wb9vv9CvDj60x0foAKqe%2BvpvEvU2769wvvU24dvhvmpmvGMJfvvmCuuQCvvyvvcBAIpvvvi4%2BvpvEvvhlWMZvvvU6dvhvmpvCtR8tvvvmsuQCvvyvvNbzjQvvvMZgvpvhvvCvpUvCvCLwPPa%2BnrMwznAMeHSSZSsIzWX49L9CvvpvvhCv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1609998280622_759&callback=jsonp760',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=594563626444&spuId=1221408307&sellerId=733274178&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvfQvfvfOvUpCkvvvvvjiWP2cytjnvP2dhsj3mPmPUsjl8PLLv0jinRLqp0jlbnUvCvCLNY%2FzJcldNzYYTaN1wN%2FYpztbwQ8QCvvDvpXWZi9Cv72u%2BvpvEphhdHbGvpH3IdvhvmZCmTCF8vhCcluQCvvDvpLUOtQCvZOe%2BvpvEphhuVhpvpHj8dvhvmZCCMBQMvhCjsOOCvvBvppvvRvhvChCvvvvvvpvVph9vvvvvmvhvLhCNcpmF%2BFBCWDAvD40XjovDN%2BL9d3ODN5HmaNopVVQHNZSh6C%2B7nDyiLO2v5fh3ZkZH1WpaRoxBnZJt9b8rwZWaUneYr2E9ZVQDYWmgvpvIphvvwvvvphCvpvF0vvCmRyCvjvUvvhBGphvwv9vvBH3vpCQmvvCh7U9CvvXmp99UjCKIvpvUphvh0J6QAt6Rvpvhvvvvv8OCvvBvpvpZdvhvmZCCWkmSvhCUt8QCvvDvpNywmQCvZyTvvpvWz%2FwiSVt4zYMNwCbwRvhvChCvvvm%2BvpvEphbEjvpvpHwPdvhvmZCC71LovhCcegvCvCLNtYrw2ldNzY%2F90M1fJYYIzTPwNL9CvvBvpvvv9vhv2nMzisz%2B7rMNz%2FeOz29CvvBvpvvv9vhv2nMSunTA7rMNzAuRzv%3D%3D&needFold=0&_ksTS=1609998327945_1486&callback=jsonp1487',

    'https://rate.tmall.com/list_detail_rate.htm?itemId=526927286858&spuId=506645136&sellerId=733274178&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvnpvfvwyvjQCkvvvvvjiWP2cytjnvRsz91jljPmP9sjnjP2qUzj1EPFFv6jkvvpvZzMJrMyC4zYMNZczGc8f5Bn%2FozWmvvpvWzMw0S8H4zYMNTHcw9vhv2nM5TlAP7rMNzt9tz8QCvvyvvjJUvvvvVjTvvpvWz%2F%2F%2BM%2B34zYMNvPPwdvhvhkpW%2FIJ8k9vW9g0zne6UgajE34QCvvyv2HOUfVQvmVe%2BvpvEvvsFm2O0vv9Q39hvCvvhvvvRvpvhvvvvvU9CvvOUvvhCJhTIvpvUvvmvRtSTbuKgvpvIvvvv2yCvvvvvvvjJphvUgpvv96CvpC29vvm2phCvhjvvvUnvphvpwv9CvhQUX7%2BvCAKDYWLhjCrQcneYiXhpVj%2BO3w0x9E9wJ9kx6acEn1vDNrBld8Q7rjlWsnsv%2B2Kz8Z0vQRAn%2BbyDCwLyTWeARFxjKOmDYb8rvvhvC9v9vvCvp29Cvvpvvvvvi9hvCvvv9U8%2BvpvEvv1F3tkOvv3kdvhvhkpWMgN6YvvWSU0zne6UgajE34QCvCUy2P%2Fj6nvv2RenrsXrmRjBAO7%2BvpvEvvQYmRqKvCC9dvhvmpvULO9Kb9vpkL9CvvpvvvvvdvhvmpvhZI93UpvOyL9Cvvpvvvvv9vhv2nMScYlj7rMNzG9%2Bz29Cvvpvvvvv&needFold=0&_ksTS=1609998383926_2062&callback=jsonp2063'
]

cookie=''