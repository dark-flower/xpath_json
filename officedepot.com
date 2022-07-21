{
  domain: "officedepot.com",

  search: {
    url: 'https://www.bhphotovideo.com/c/search?q={{query}}&sts=ma',
    scrape: {
      resultContainer: './/div[contains(@class,"sku_item")]',
      cost: './/span[@class="price_column right")]/text()',
      image: './/div[@class="photo_no_QV flcl")]/a/img/@src',
      title: './/div[@class="desc_text")]/a/text()',
      URL: './/div[@class="desc_text")]/a/@href',
    }
  },

  product: {
    title: "//h1[@itemprop='name']/text()",
    cost: "//span[@class='od-graphql-price-big-price']/text()",
    delivery: "//div[@class='od-container od-container-lg']//text()",
    brand: "substring-after('"brand":"','')",
    //condition: "substring-after('isRefurbished&quot;','')",
    availability: "substring-after('"availability":"','')",
    mpn: "substring-after('"mpn":"','')",
  },

  productPaths: [
    https./\/(.+)\/([^\/]+?),
  ],

  exampleProductPages: [{
      "url": "https://www.officedepot.com/a/products/458914/Duracell-Coppertop-AA-Alkaline-Batteries-Pack/",
      "cost": "$31.99",
      "brand": "Duracell",
      "title": "Duracell® Coppertop AA Alkaline Batteries, Pack Of 24",
    },
    {
      "kind": "product",
      "availability": "https://schema.org/InStock",
      "cost": {
        "currency": "USD",
        "retailer": 239.99
      },
      "brand": "Realspace",
      "title": "Realspace® Fennington Bonded Leather High-Back Executive Chair, Black",
      "url": "https://www.officedepot.com/a/products/633410/Realspace-Fennington-Bonded-Leather-High-Back/"
    }

  ]
}
