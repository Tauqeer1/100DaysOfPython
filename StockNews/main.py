import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

dummy_data = {
  'Meta Data': {
    '1. Information': 'Daily Prices (open, high, low, close) and Volumes',
    '2. Symbol': 'TSLA',
    '3. Last Refreshed': '2025-05-12',
    '4. Output Size': 'Compact',
    '5. Time Zone': 'US/Eastern'
  },
  'Time Series (Daily)': {
    '2025-05-12': {
      '1. open': '321.9900',
      '2. high': '322.2100',
      '3. low': '311.5000',
      '4. close': '318.3800',
      '5. volume': '112826661'
    },
    '2025-05-09': {
      '1. open': '290.2100',
      '2. high': '307.0400',
      '3. low': '290.0000',
      '4. close': '298.2600',
      '5. volume': '132387835'
    },
    '2025-05-08': {
      '1. open': '279.6300',
      '2. high': '289.8000',
      '3. low': '279.4100',
      '4. close': '284.8200',
      '5. volume': '97539448'
    },
    '2025-05-07': {
      '1. open': '276.8800',
      '2. high': '277.9200',
      '3. low': '271.0000',
      '4. close': '276.2200',
      '5. volume': '71882408'
    },
    '2025-05-06': {
      '1. open': '273.1050',
      '2. high': '277.7300',
      '3. low': '271.3500',
      '4. close': '275.3500',
      '5. volume': '76715792'
    },
    '2025-05-05': {
      '1. open': '284.5700',
      '2. high': '284.8490',
      '3. low': '274.4000',
      '4. close': '280.2600',
      '5. volume': '94618882'
    },
    '2025-05-02': {
      '1. open': '284.9000',
      '2. high': '294.7800',
      '3. low': '279.8100',
      '4. close': '287.2100',
      '5. volume': '114454683'
    },
    '2025-05-01': {
      '1. open': '280.0100',
      '2. high': '290.8688',
      '3. low': '279.8100',
      '4. close': '280.5200',
      '5. volume': '99658974'
    },
    '2025-04-30': {
      '1. open': '279.9000',
      '2. high': '284.4500',
      '3. low': '270.7800',
      '4. close': '282.1600',
      '5. volume': '128961057'
    },
    '2025-04-29': {
      '1. open': '285.5000',
      '2. high': '293.3200',
      '3. low': '279.4695',
      '4. close': '292.0300',
      '5. volume': '108906553'
    },
    '2025-04-28': {
      '1. open': '288.9800',
      '2. high': '294.8600',
      '3. low': '272.4200',
      '4. close': '285.8800',
      '5. volume': '151731771'
    },
    '2025-04-25': {
      '1. open': '261.6900',
      '2. high': '286.8500',
      '3. low': '259.6300',
      '4. close': '284.9500',
      '5. volume': '167560688'
    },
    '2025-04-24': {
      '1. open': '250.5000',
      '2. high': '259.5400',
      '3. low': '249.2000',
      '4. close': '259.5100',
      '5. volume': '94464195'
    },
    '2025-04-23': {
      '1. open': '254.8600',
      '2. high': '259.4499',
      '3. low': '244.4300',
      '4. close': '250.7400',
      '5. volume': '150381903'
    },
    '2025-04-22': {
      '1. open': '230.9600',
      '2. high': '242.7900',
      '3. low': '229.8501',
      '4. close': '237.9700',
      '5. volume': '120858452'
    },
    '2025-04-21': {
      '1. open': '230.2600',
      '2. high': '232.2100',
      '3. low': '222.7900',
      '4. close': '227.5000',
      '5. volume': '97768007'
    },
    '2025-04-17': {
      '1. open': '243.4700',
      '2. high': '244.3400',
      '3. low': '237.6833',
      '4. close': '241.3700',
      '5. volume': '83404775'
    },
    '2025-04-16': {
      '1. open': '247.6100',
      '2. high': '251.9700',
      '3. low': '233.8900',
      '4. close': '241.5500',
      '5. volume': '112378737'
    },
    '2025-04-15': {
      '1. open': '249.9100',
      '2. high': '258.7500',
      '3. low': '247.5400',
      '4. close': '254.1100',
      '5. volume': '79594318'
    },
    '2025-04-14': {
      '1. open': '258.3600',
      '2. high': '261.8000',
      '3. low': '245.9300',
      '4. close': '252.3500',
      '5. volume': '100135241'
    },
    '2025-04-11': {
      '1. open': '251.8400',
      '2. high': '257.7400',
      '3. low': '241.3629',
      '4. close': '252.3100',
      '5. volume': '128948085'
    },
    '2025-04-10': {
      '1. open': '260.0000',
      '2. high': '262.4900',
      '3. low': '239.3300',
      '4. close': '252.4000',
      '5. volume': '181722604'
    },
    '2025-04-09': {
      '1. open': '224.6900',
      '2. high': '274.6900',
      '3. low': '223.8800',
      '4. close': '272.2000',
      '5. volume': '219433373'
    },
    '2025-04-08': {
      '1. open': '245.0000',
      '2. high': '250.4400',
      '3. low': '217.8000',
      '4. close': '221.8600',
      '5. volume': '171603472'
    },
    '2025-04-07': {
      '1. open': '223.7800',
      '2. high': '252.0000',
      '3. low': '214.2500',
      '4. close': '233.2900',
      '5. volume': '183453776'
    },
    '2025-04-04': {
      '1. open': '255.3800',
      '2. high': '261.0000',
      '3. low': '236.0000',
      '4. close': '239.4300',
      '5. volume': '181229353'
    },
    '2025-04-03': {
      '1. open': '265.2900',
      '2. high': '276.3000',
      '3. low': '261.5100',
      '4. close': '267.2800',
      '5. volume': '136174291'
    },
    '2025-04-02': {
      '1. open': '254.6000',
      '2. high': '284.9900',
      '3. low': '251.2700',
      '4. close': '282.7600',
      '5. volume': '212787817'
    },
    '2025-04-01': {
      '1. open': '263.8000',
      '2. high': '277.4500',
      '3. low': '259.2500',
      '4. close': '268.4600',
      '5. volume': '146486911'
    },
    '2025-03-31': {
      '1. open': '249.3100',
      '2. high': '260.5600',
      '3. low': '243.3601',
      '4. close': '259.1600',
      '5. volume': '134008936'
    },
    '2025-03-28': {
      '1. open': '275.5750',
      '2. high': '276.1000',
      '3. low': '260.5700',
      '4. close': '263.5500',
      '5. volume': '123809389'
    },
    '2025-03-27': {
      '1. open': '272.4800',
      '2. high': '291.8500',
      '3. low': '271.8216',
      '4. close': '273.1300',
      '5. volume': '162572146'
    },
    '2025-03-26': {
      '1. open': '282.6600',
      '2. high': '284.9000',
      '3. low': '266.5100',
      '4. close': '272.0600',
      '5. volume': '156254441'
    },
    '2025-03-25': {
      '1. open': '283.6000',
      '2. high': '288.2000',
      '3. low': '271.2800',
      '4. close': '288.1400',
      '5. volume': '150361538'
    },
    '2025-03-24': {
      '1. open': '258.0750',
      '2. high': '278.6400',
      '3. low': '256.3300',
      '4. close': '278.3900',
      '5. volume': '169079865'
    },
    '2025-03-21': {
      '1. open': '234.9850',
      '2. high': '249.5200',
      '3. low': '234.5500',
      '4. close': '248.7100',
      '5. volume': '132728684'
    },
    '2025-03-20': {
      '1. open': '233.3450',
      '2. high': '238.0000',
      '3. low': '230.0501',
      '4. close': '236.2600',
      '5. volume': '99028270'
    },
    '2025-03-19': {
      '1. open': '231.6100',
      '2. high': '241.4100',
      '3. low': '229.2010',
      '4. close': '235.8600',
      '5. volume': '111993753'
    },
    '2025-03-18': {
      '1. open': '228.1550',
      '2. high': '230.1000',
      '3. low': '222.2800',
      '4. close': '225.3100',
      '5. volume': '111477636'
    },
    '2025-03-17': {
      '1. open': '245.0550',
      '2. high': '245.4000',
      '3. low': '232.8000',
      '4. close': '238.0100',
      '5. volume': '111900565'
    },
    '2025-03-14': {
      '1. open': '247.3100',
      '2. high': '251.5800',
      '3. low': '240.7300',
      '4. close': '249.9800',
      '5. volume': '100242264'
    },
    '2025-03-13': {
      '1. open': '248.1250',
      '2. high': '248.2900',
      '3. low': '232.6000',
      '4. close': '240.6800',
      '5. volume': '114813525'
    },
    '2025-03-12': {
      '1. open': '247.2200',
      '2. high': '251.8400',
      '3. low': '241.1000',
      '4. close': '248.0900',
      '5. volume': '142215681'
    },
    '2025-03-11': {
      '1. open': '225.3050',
      '2. high': '237.0649',
      '3. low': '217.0200',
      '4. close': '230.5800',
      '5. volume': '174896415'
    },
    '2025-03-10': {
      '1. open': '252.5400',
      '2. high': '253.3700',
      '3. low': '220.0000',
      '4. close': '222.1500',
      '5. volume': '185037825'
    },
    '2025-03-07': {
      '1. open': '259.3200',
      '2. high': '266.2499',
      '3. low': '250.7300',
      '4. close': '262.6700',
      '5. volume': '102369640'
    },
    '2025-03-06': {
      '1. open': '272.0600',
      '2. high': '272.6500',
      '3. low': '260.0200',
      '4. close': '263.4500',
      '5. volume': '98451566'
    },
    '2025-03-05': {
      '1. open': '272.9200',
      '2. high': '279.5500',
      '3. low': '267.7100',
      '4. close': '279.1000',
      '5. volume': '94042913'
    },
    '2025-03-04': {
      '1. open': '270.9300',
      '2. high': '284.3500',
      '3. low': '261.8401',
      '4. close': '272.0400',
      '5. volume': '126706623'
    },
    '2025-03-03': {
      '1. open': '300.3400',
      '2. high': '303.9400',
      '3. low': '277.3000',
      '4. close': '284.6500',
      '5. volume': '115551414'
    },
    '2025-02-28': {
      '1. open': '279.5000',
      '2. high': '293.8800',
      '3. low': '273.6000',
      '4. close': '292.9800',
      '5. volume': '115696968'
    },
    '2025-02-27': {
      '1. open': '291.1600',
      '2. high': '297.2300',
      '3. low': '280.8800',
      '4. close': '281.9500',
      '5. volume': '101748197'
    },
    '2025-02-26': {
      '1. open': '303.7150',
      '2. high': '309.0000',
      '3. low': '288.0400',
      '4. close': '290.8000',
      '5. volume': '100118276'
    },
    '2025-02-25': {
      '1. open': '327.0250',
      '2. high': '328.8900',
      '3. low': '297.2512',
      '4. close': '302.8000',
      '5. volume': '134228777'
    },
    '2025-02-24': {
      '1. open': '338.1400',
      '2. high': '342.3973',
      '3. low': '324.7000',
      '4. close': '330.5300',
      '5. volume': '76052321'
    },
    '2025-02-21': {
      '1. open': '353.4400',
      '2. high': '354.9800',
      '3. low': '334.4200',
      '4. close': '337.8000',
      '5. volume': '74058648'
    },
    '2025-02-20': {
      '1. open': '361.5100',
      '2. high': '362.3000',
      '3. low': '348.0000',
      '4. close': '354.4000',
      '5. volume': '45965354'
    },
    '2025-02-19': {
      '1. open': '354.0000',
      '2. high': '367.3400',
      '3. low': '353.6700',
      '4. close': '360.5600',
      '5. volume': '67094374'
    },
    '2025-02-18': {
      '1. open': '355.0100',
      '2. high': '359.1000',
      '3. low': '350.0200',
      '4. close': '354.1100',
      '5. volume': '51631702'
    },
    '2025-02-14': {
      '1. open': '360.6200',
      '2. high': '362.0000',
      '3. low': '347.5000',
      '4. close': '355.8400',
      '5. volume': '68277279'
    },
    '2025-02-13': {
      '1. open': '345.0000',
      '2. high': '358.6900',
      '3. low': '342.8500',
      '4. close': '355.9400',
      '5. volume': '89441519'
    },
    '2025-02-12': {
      '1. open': '329.9400',
      '2. high': '346.4000',
      '3. low': '329.1200',
      '4. close': '336.5100',
      '5. volume': '105382729'
    },
    '2025-02-11': {
      '1. open': '345.8000',
      '2. high': '349.3700',
      '3. low': '325.1000',
      '4. close': '328.5000',
      '5. volume': '118543400'
    },
    '2025-02-10': {
      '1. open': '356.2100',
      '2. high': '362.7000',
      '3. low': '350.5100',
      '4. close': '350.7300',
      '5. volume': '77514903'
    },
    '2025-02-07': {
      '1. open': '370.1900',
      '2. high': '380.5459',
      '3. low': '360.3400',
      '4. close': '361.6200',
      '5. volume': '70298258'
    },
    '2025-02-06': {
      '1. open': '373.0300',
      '2. high': '375.4000',
      '3. low': '363.1800',
      '4. close': '374.3200',
      '5. volume': '77918230'
    },
    '2025-02-05': {
      '1. open': '387.5100',
      '2. high': '388.3900',
      '3. low': '375.5300',
      '4. close': '378.1700',
      '5. volume': '57614721'
    },
    '2025-02-04': {
      '1. open': '382.6300',
      '2. high': '394.0000',
      '3. low': '381.4000',
      '4. close': '392.2100',
      '5. volume': '57072235'
    },
    '2025-02-03': {
      '1. open': '386.6800',
      '2. high': '389.1700',
      '3. low': '374.3600',
      '4. close': '383.6800',
      '5. volume': '93732122'
    },
    '2025-01-31': {
      '1. open': '401.5300',
      '2. high': '419.9900',
      '3. low': '401.3400',
      '4. close': '404.6000',
      '5. volume': '83568219'
    },
    '2025-01-30': {
      '1. open': '410.7800',
      '2. high': '412.5000',
      '3. low': '384.4100',
      '4. close': '400.2800',
      '5. volume': '98092879'
    },
    '2025-01-29': {
      '1. open': '395.2100',
      '2. high': '398.5899',
      '3. low': '384.4800',
      '4. close': '389.1000',
      '5. volume': '68033648'
    },
    '2025-01-28': {
      '1. open': '396.9100',
      '2. high': '400.5900',
      '3. low': '386.5000',
      '4. close': '398.0900',
      '5. volume': '48910676'
    },
    '2025-01-27': {
      '1. open': '394.8000',
      '2. high': '406.6900',
      '3. low': '389.0000',
      '4. close': '397.1500',
      '5. volume': '58125510'
    },
    '2025-01-24': {
      '1. open': '414.4500',
      '2. high': '418.8800',
      '3. low': '405.7800',
      '4. close': '406.5800',
      '5. volume': '56427149'
    },
    '2025-01-23': {
      '1. open': '416.0600',
      '2. high': '420.7300',
      '3. low': '408.9500',
      '4. close': '412.3800',
      '5. volume': '50690592'
    },
    '2025-01-22': {
      '1. open': '416.8100',
      '2. high': '428.0000',
      '3. low': '414.5900',
      '4. close': '415.1100',
      '5. volume': '60963342'
    },
    '2025-01-21': {
      '1. open': '432.6400',
      '2. high': '433.2000',
      '3. low': '406.3100',
      '4. close': '424.0700',
      '5. volume': '87320894'
    },
    '2025-01-17': {
      '1. open': '421.5000',
      '2. high': '439.7400',
      '3. low': '419.7500',
      '4. close': '426.5000',
      '5. volume': '94991429'
    },
    '2025-01-16': {
      '1. open': '423.4900',
      '2. high': '424.0000',
      '3. low': '409.1300',
      '4. close': '413.8200',
      '5. volume': '68335151'
    },
    '2025-01-15': {
      '1. open': '409.9000',
      '2. high': '429.8000',
      '3. low': '405.6610',
      '4. close': '428.2200',
      '5. volume': '81375460'
    },
    '2025-01-14': {
      '1. open': '414.3400',
      '2. high': '422.6400',
      '3. low': '394.5400',
      '4. close': '396.3600',
      '5. volume': '84565022'
    },
    '2025-01-13': {
      '1. open': '383.2100',
      '2. high': '403.7900',
      '3. low': '380.0700',
      '4. close': '403.3100',
      '5. volume': '67580494'
    },
    '2025-01-10': {
      '1. open': '391.4000',
      '2. high': '399.2800',
      '3. low': '377.2900',
      '4. close': '394.7400',
      '5. volume': '62287333'
    },
    '2025-01-08': {
      '1. open': '392.9500',
      '2. high': '402.4999',
      '3. low': '387.4000',
      '4. close': '394.9400',
      '5. volume': '73038805'
    },
    '2025-01-07': {
      '1. open': '405.8300',
      '2. high': '414.3300',
      '3. low': '390.0000',
      '4. close': '394.3600',
      '5. volume': '75699525'
    },
    '2025-01-06': {
      '1. open': '423.2000',
      '2. high': '426.4300',
      '3. low': '401.7000',
      '4. close': '411.0500',
      '5. volume': '85516534'
    },
    '2025-01-03': {
      '1. open': '381.4800',
      '2. high': '411.8799',
      '3. low': '379.4500',
      '4. close': '410.4400',
      '5. volume': '95423329'
    },
    '2025-01-02': {
      '1. open': '390.1000',
      '2. high': '392.7299',
      '3. low': '373.0400',
      '4. close': '379.2800',
      '5. volume': '109710749'
    },
    '2024-12-31': {
      '1. open': '423.7900',
      '2. high': '427.9300',
      '3. low': '402.5400',
      '4. close': '403.8400',
      '5. volume': '76825121'
    },
    '2024-12-30': {
      '1. open': '419.4000',
      '2. high': '427.0000',
      '3. low': '415.7500',
      '4. close': '417.4100',
      '5. volume': '64941012'
    },
    '2024-12-27': {
      '1. open': '449.5200',
      '2. high': '450.0000',
      '3. low': '426.5000',
      '4. close': '431.6600',
      '5. volume': '82666821'
    },
    '2024-12-26': {
      '1. open': '465.1600',
      '2. high': '465.3299',
      '3. low': '451.0200',
      '4. close': '454.1300',
      '5. volume': '76651210'
    },
    '2024-12-24': {
      '1. open': '435.9000',
      '2. high': '462.7800',
      '3. low': '435.1400',
      '4. close': '462.2800',
      '5. volume': '59551750'
    },
    '2024-12-23': {
      '1. open': '431.0000',
      '2. high': '434.5100',
      '3. low': '415.4112',
      '4. close': '430.6000',
      '5. volume': '72698055'
    },
    '2024-12-20': {
      '1. open': '425.5050',
      '2. high': '447.0800',
      '3. low': '417.6400',
      '4. close': '421.0600',
      '5. volume': '132216176'
    },
    '2024-12-19': {
      '1. open': '451.8800',
      '2. high': '456.3600',
      '3. low': '420.0200',
      '4. close': '436.1700',
      '5. volume': '118566146'
    },
    '2024-12-18': {
      '1. open': '466.4950',
      '2. high': '488.5399',
      '3. low': '427.0100',
      '4. close': '440.1300',
      '5. volume': '149340788'
    },
    '2024-12-17': {
      '1. open': '475.9000',
      '2. high': '483.9900',
      '3. low': '457.5101',
      '4. close': '479.8600',
      '5. volume': '131222978'
    },
    '2024-12-16': {
      '1. open': '441.0900',
      '2. high': '463.1900',
      '3. low': '436.1500',
      '4. close': '463.0200',
      '5. volume': '114083811'
    }
  }
}

stock_api_key = "KGD5ABHQ354YQI8C"
news_api_key = "1e8dfd80c66f43d0916dddd78083006d"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "apikey": stock_api_key,
    "symbol": STOCK_NAME,
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# stock_request = requests.get(STOCK_ENDPOINT, params=stock_params)
# stock_request.raise_for_status()
# stock_response = stock_request.json()
# print(stock_response)
# stock_data = stock_response["Time Series (Daily)"]
stock_data = dummy_data["Time Series (Daily)"]
stock_prices = [value for key, value in stock_data.items()]

yesterday_stock_price = stock_prices[0]
yesterday_closing_price = float(yesterday_stock_price["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_stock_price = stock_prices[1]
day_before_yesterday_closing_price = float(day_before_yesterday_stock_price["4. close"])


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff_between_prices = abs(yesterday_closing_price - day_before_yesterday_closing_price)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = (diff_between_prices / yesterday_closing_price) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 5:
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME, "apiKey": news_api_key
    }
    news_request = requests.get(NEWS_ENDPOINT, params=news_params)
    news_request.raise_for_status()
    news_response = news_request.json()
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three_articles_data = news_response["articles"][:3]
    print(first_three_articles_data)

    new_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles_data]
    print(new_list)








    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

