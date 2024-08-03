function main(item) {
    const url = item.url;
    const id = jz.getQuery(item.url, "channel-id");
    const res = jz.getHeaders(url, false);
    const location = res.ResponseHeaders.location;
    const uri = jz.Uri(location);
    let domain;
    switch (id) {
        case "wasusyt":
            //domain = 'http://cache.ott.wasulive.itv.cmvideo.cn'
            domain = 'http://pixman.io.wasulive.dnsany.com'
            break;
        case "bestzb":
            //domain = 'http://cache.ott.bestlive.itv.cmvideo.cn'
            //domain = 'http://mglivesu.hometv.komect.com'
            domain = 'http://pixman.io.bestlive.dnsany.com'
            break;
        case "ystenlive":
            //domain = 'http://cache.ott.ystenlive.itv.cmvideo.cn'
            domain = 'http://pixman.io.ystenlive.dnsany.com'
            break;
        case "hnbblive":
            //domain = 'http://cache.ott.hnbblive.itv.cmvideo.cn'
            domain = 'http://pixman.io.hnbblive.dnsany.com'
            break;
        case "FifastbLive":
            //domain = 'http://cache.ott.fifalive.itv.cmvideo.cn'
            domain = 'http://pixman.io.fifalive.ottdns.com'
            break;
    }
    return { url: domain + uri.FullPath + '?' + uri.Query };
}