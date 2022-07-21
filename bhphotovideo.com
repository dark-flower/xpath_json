{
  domain: "bhphotovideo.com",

  search: {
    url: 'https://www.bhphotovideo.com/c/search?q={{query}}&sts=ma',
    scrape: {
      resultContainer: './/div[@data-selenium="miniProductPage")]',
      cost: './/span[@data-selenium="uppedDecimalPriceFirst")]',
      image: './/img[@data-selenium="miniProductPageImg")]',
      title: './/span[@data-selenium="miniProductPageProductName")]',
      URL: './/a[@data-selenium="miniProductPageProductNameLink")]/@href',
    }
  },

  product: {
    title: "//h1[@data-selenium='productTitle']/text()",
    cost: "//div[@data-selenium='pricingPrice']/text()",
    delivery: "//div[@class='shipInfoLayer']//text()",
    brand: "substring-after('@type":"Brand","name":"','')",
    condition: "substring-after('isRefurbished&quot;','')",
    availability: "//div[@class='stockStatus']/text()",
    barcode: "substring-after(//div[@data-selenium='overviewUpcText'],'UPC: ')",
    mpn: "substring-after('"mpn":"','')",
  },

  productPaths: [
    /\/(.+)\/([^\/]+?)\/(?<identifier>[\w+]+)\.html/,
  ],

  exampleProductPages: [{
      "url": "https://www.bhphotovideo.com/c/product/1437100-REG/asus_xonar_se_5_1_channel.html",
      "cost": "$39.99",
      "barcode": "192876040560",
      "brand": "ASUS",
      "title": "ASUS Xonar SE 5.1-Channel PCIe Gaming Sound Card",
    },
    {
      "kind": "product",
      "availability": "Special Order",
      "cost": {
        "currency": "USD",
        "retailer": 286.95
      },
      "barcode": "887276324272",
      "brand": "Samsung",
      "title": "Samsung Flat Wall Mount for Select Samsung Displays",
      "url": "https://www.bhphotovideo.com/c/product/1541637-REG/samsung_wmn6575se_wall_mount_for.html"
    }

  ]
}
