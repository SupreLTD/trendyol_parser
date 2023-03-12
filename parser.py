import grequests
import requests
from tqdm import tqdm

import pandas as pd


class Parser:
    def __init__(self, brand, name_brand):
        self.brand = brand
        self.name_brand = name_brand

    def get_all_item_id(self):

        ids = []
        if self.brand.startswith('mid'):
            items_count = requests.get(
                f'https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr?{self.brand}&' 
                f'os=1&pi=1&culture=tr-TR&userGenderId=1&pId=0&scoringAlgorithmId=2&categoryRelevancyEnabled=false&is'
                f'LegalRequirementConfirmed=false&searchStrategyType=DEFAULT&productStampType=TypeA&fixSlotProductAds'
                f'Included=true&searchAbDecider=%2CSuggestion_A%2CRelevancy_1%2CFilterRelevancy_1%2CListingScoringAlgo'
                f'rithmId_1%2CSmartlisting_2%2CFlashSales_1%2CSuggestionBadges_A').json()['result']['totalCount']
            if items_count % 24 != 0:
                count = items_count // 24 + 1
            else:
                count = items_count // 24
            links = [f'https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-' \
                     f'scroll/sr?{self.brand}&os=1&sk=1&pi={i}&culture=tr-TR&userGenderId=1&pId=0&scoringAlgorithmId=2' \
                     f'&categoryRelevancyEnabled=false&isLegalRequirementConfirmed=false&searchStrategyType=DEFAULT&' \
                     f'productStampType=TypeA&fixSlotProductAdsIncluded=true&searchAbDecider=%2CSuggestion_A%2' \
                     f'CRelevancy_1%2CFilterRelevancy_1%2CListingScoringAlgorithmId_1%2CSmartlisting_2%2' \
                     f'CFlashSales_1%2CSuggestionBadges_A&offset=' for i in range(1, count + 1)]
            response = (grequests.get(url) for url in links)
            for link in tqdm(grequests.map(response)):
                ids.extend([i['id'] for i in link.json()['result']['products']])

        else:
            items_count = requests.get(
                f'https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr?{self.brand}&'
                f'os=1&sk=1&pi=2&culture=tr-TR&userGenderId=1&pId=0&scoringAlgorithmId=2&categoryRelevancyEnabled=false'
                f'&isLegalRequirementConfirmed=false&searchStrategyType=DEFAULT&productStampType=TypeA&fixSlotProduct'
                f'AdsIncluded=true&searchAbDecider=%2CSuggestion_A%2CRelevancy_1%2CFilterRelevancy_1%2CListingScoring'
                f'AlgorithmId_1%2CSmartlisting_2%2CFlash'
                f'Sales_1%2CSuggestionBadges_A&offset=0').json()['result']['totalCount']
            if items_count % 24 != 0:
                count = items_count // 24 + 1
            else:
                count = items_count // 24
            links = [
                f'https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr?{self.brand}&os=1&sk=1&pi=2&culture=tr-TR&userGenderId=1&pId=0&scoringAlgorithmId=2&categoryRelevancyEnabled=false&isLegalRequirementConfirmed=false&searchStrategyType=DEFAULT&productStampType=TypeA&fixSlotProductAdsIncluded=true&searchAbDecider=%2CSuggestion_A%2CRelevancy_1%2CFilterRelevancy_1%2CListingScoringAlgorithmId_1%2CSmartlisting_2%2CFlashSales_1%2CSuggestionBadges_A&offset={str(i * 24)}'
                for i in range(0, count + 1)]
            response = (grequests.get(url) for url in links)
            for link in tqdm(grequests.map(response)):
                ids.extend([i['id'] for i in link.json()['result']['products']])
        return ids

    def get_data(self, ids):
        items = []
        links = [
            f'https://public.trendyol.com/discovery-web-productgw-service/api/productDetail/{item}?sav=false&storefrontId=1&culture=tr-TR&linearVariants=true&isLegalRequirementConfirmed=false'
            for item in tqdm(ids)]
        response = (grequests.get(url) for url in tqdm(links))
        for item in tqdm(grequests.map(response)):
            try:
                res = item.json()['result']
                name = res['name']
                category = res['category']['hierarchy'].split('/')
                shoes = ['Sneaker', 'Bot', 'Klasik Topuklu', 'Ayakkabı', 'Terlik', 'Sandalet']
                main_category = category[0]
                under_category = category[1]
                last_category = category[-1]
                brand = res['brand']['name']
                if main_category not in shoes:
                    wear_size = ','.join([i['value'] for i in res['allVariants']])
                else:
                    wear_size = ''
                images = ','.join(['https://cdn.dsmcdn.com' + i for i in res['images']])
                if main_category in shoes:
                    shoe_size = ','.join([i['value'] for i in res['allVariants']])
                else:
                    shoe_size = ''
                price = res['price']['discountedPrice']['value']
                sizes = ','.join([i['value'] for i in res['allVariants'] if i['inStock']])
                url = 'https://www.trendyol.com' + res['url']
                try:
                    sex = 'Мужской' if res['gender']['name'].lower() == 'erkek' else 'Женский' \
                        if res['gender']['name'].lower() == 'kadın' else 'Унисекс'
                except Exception as e:
                    sex = 'Унисекс'
                article = res['id']
                color = res['color']
                params = {i['key']['name']: i['value']['name'] for i in res['attributes']}
                try:
                    out_material = params['Dış Materyal']
                except Exception as e:
                    out_material = ''
                try:
                    goal = params['Kullanım Alanı']
                except Exception as e:
                    goal = ''
                try:
                    Advantage = params['Taban Teknolojisi']
                except Exception as e:
                    Advantage = ''
                try:
                    Binding = params['Bağlama Şekli']
                except Exception as e:
                    Binding = ''
                try:
                    Outsole = params['Taban Materyali']
                except Exception as e:
                    Outsole = ''
                try:
                    material = params['Materyal']
                except Exception as e:
                    material = ''
                try:
                    form = params['Kalıp']
                except Exception as e:
                    form = ''
                try:
                    complect = params['Paket İçeriği']
                except Exception as e:
                    complect = ''
                try:
                    collection = params['Koleksiyon']
                except Exception as e:
                    collection = ''
                try:
                    Arm_Type = params['Kol Tipi']
                except Exception as e:
                    Arm_Type = ''
                try:
                    Fabric_Type = params['Kumaş Tipi']
                except Exception as e:
                    Fabric_Type = ''
                try:
                    style = params['Stil']
                except Exception as e:
                    style = ''
                try:
                    Fabric_Technology = params['Kumaş Teknolojisi']
                except Exception as e:
                    Fabric_Technology = ''
                try:
                    Size_Dimension = params['Boy / Ölçü']
                except Exception as e:
                    Size_Dimension = ''
                try:
                    Product_Type = params['Ürün Tipi']
                except Exception as e:
                    Product_Type = ''
                try:
                    Arm_Length = params['Kol Boyu']
                except Exception as e:
                    Arm_Length = ''
                try:
                    Thickness = params['Kalınlık']
                except Exception as e:
                    Thickness = ''
                try:
                    size = params['Boy']
                except Exception as e:
                    size = ''
                try:
                    Ambient = params['Ortam']
                except Exception as e:
                    Ambient = ''
                try:
                    Number_of_Parts = params['Parça Sayısı']
                except Exception as e:
                    Number_of_Parts = ''
                try:
                    Persona = params['Persona']
                except Exception as e:
                    Persona = ''
                try:
                    back_size = params['Beden']
                except Exception as e:
                    back_size = ''
                try:
                    Base_Type = params['Taban Tipi']
                except Exception as e:
                    Base_Type = ''
                try:
                    Heel_Type = params['Topuk Tipi']
                except Exception as e:
                    Heel_Type = ''
                try:
                    Feature = params['Özellik']
                except Exception as e:
                    Feature = ''
                try:
                    Fabric_Feature = params['Kumaş Özellik']
                except Exception as e:
                    Fabric_Feature = ''
                try:
                    Leg_Type = params['Paça Tipi']
                except Exception as e:
                    Leg_Type = ''
                try:
                    Leg_Length = params['Paça Boyu']
                except Exception as e:
                    Leg_Length = ''
                try:
                    Waist = params['Bel']
                except Exception as e:
                    Waist = ''
                try:
                    Type = params['Tip']
                except Exception as e:
                    Type = ''
                try:
                    School = params['Okula Dönüş']
                except Exception as e:
                    School = ''
                try:
                    Pattern = params['Desen']
                except Exception as e:
                    Pattern = ''
                try:
                    Capacity = params['Kapasite']
                except Exception as e:
                    Capacity = ''
                try:
                    Sport_Branch = params['Spor Branşı']
                except Exception as e:
                    Sport_Branch = ''
                try:
                    Closing_Shape = params['Kapama Şekli']
                except Exception as e:
                    Closing_Shape = ''
                try:
                    Collar_Type = params['Yaka Tipi']
                except Exception as e:
                    Collar_Type = ''
                try:
                    Model = params['Model']
                except Exception as e:
                    Model = ''
                try:
                    Cutting = params['Kesim']
                except Exception as e:
                    Cutting = ''
                try:
                    Sport_Type = params['Spor Türü']
                except Exception as e:
                    Sport_Type = ''
                try:
                    Liner_Condition = params['Astar Durumu']
                except Exception as e:
                    Liner_Condition = ''
                try:
                    Sustainability_Detail = params['Sürdürülebilirlik Detayı']
                except Exception as e:
                    Sustainability_Detail = ''
                try:
                    Upper_Material = params['Saya Materyali']
                except Exception as e:
                    Upper_Material = ''
                try:
                    Heel_Height = params['Topuk Boyu']
                except Exception as e:
                    Heel_Height = ''
                try:
                    Insole_Material = params['İç Taban Materyali']
                except Exception as e:
                    Insole_Material = ''
                try:
                    Lining_Material = params['Astar Materyali']
                except Exception as e:
                    Lining_Material = ''
                try:
                    Leather_Quality = params['Deri Kalitesi']
                except Exception as e:
                    Leather_Quality = ''
                try:
                    Additional_Feature = params['Ek Özellik']
                except Exception as e:
                    Additional_Feature = ''
                try:
                    Filler = params['İzolasyon']
                except Exception as e:
                    Filler = ''
                try:
                    Sustainable = params['Sürdürülebilir']
                except Exception as e:
                    Sustainable = ''
                try:
                    Pocket_Type = params['Cep Tipi']
                except Exception as e:
                    Pocket_Type = ''
                try:
                    Pocket = params['Cep']
                except Exception as e:
                    Pocket = ''
                try:
                    Floor = params['Zemin']
                except Exception as e:
                    Floor = ''
                try:
                    Nail_Type = params['Çivi Tipi']
                except Exception as e:
                    Nail_Type = ''
                try:
                    Variety = params['Çeşit']
                except Exception as e:
                    Variety = ''
                try:
                    Wrist_Style = params['Bilek Stili']
                except Exception as e:
                    Wrist_Style = ''
                try:
                    Product_Details = params['Ürün Detayı']
                except Exception as e:
                    Product_Details = ''
                try:
                    Cord_Status = params['Kordon Durumu'] = ''
                except Exception as e:
                    Cord_Status = ''
                try:
                    Silhouette = params['Siluet']
                except Exception as e:
                    Silhouette = ''
                try:
                    Bag_size = params['Boyut']
                except Exception as e:
                    Bag_size = ''
                try:
                    Yarn_Feature = params['Kumaş/İplik Özellik']
                except Exception as e:
                    Yarn_Feature = ''
                try:
                    Technical = params['Teknik']
                except Exception as e:
                    Technical = ''
                try:
                    Bottom_Upper_Team = params['Alt-Üst Takım']
                except Exception as e:
                    Bottom_Upper_Team = ''
                try:
                    Belt = params['Kemer/Kuşak Durumu']
                except Exception as e:
                    Belt = ''
                try:
                    Shoe_Sole = params['Ayakkabı Tabanı']
                except Exception as e:
                    Shoe_Sole = ''
                try:
                    Sole_Material = params['Taban']
                except Exception as e:
                    Sole_Material = ''
                try:
                    Pocket_Number = params['Cep Sayısı']
                except Exception as e:
                    Pocket_Number = ''
                try:
                    Filling_Technique = params['Dolgu Tekniği']
                except Exception as e:
                    Filling_Technique = ''
                try:
                    Filling_Material = params['Dolgu Materyali']
                except Exception as e:
                    Filling_Material = ''
                try:
                    Branch = params['Branş']
                except Exception as e:
                    Branch = ''
                try:
                    Weaving_Type = params['Dokuma Tipi']
                except Exception as e:
                    Weaving_Type = ''
                try:
                    Printing_Technique = params['Baskı/Nakış Tekniği']
                except Exception as e:
                    Printing_Technique = ''
                try:
                    Equalization = params['Ekartman']
                except Exception as e:
                    Equalization = ''
                try:
                    Glass_Material = params['Cam Materyali']
                except Exception as e:
                    Glass_Material = ''
                try:
                    Frame_Material = params['Çerçeve Materyali']
                except Exception as e:
                    Frame_Material = ''
                try:
                    Glass_Type = params['Cam Tipi']
                except Exception as e:
                    Glass_Type = ''
                try:
                    Frame_Form = params['Çerçeve Formu']
                except Exception as e:
                    Frame_Form = ''
                try:
                    Glass_Color = params['Cam Renk']
                except Exception as e:
                    Glass_Color = ''
                try:
                    Frame_Color = params['Çerçeve Renk']
                except Exception as e:
                    Frame_Color = ''
                try:
                    Frame_Type = params['Çerçeve Tipi']
                except Exception as e:
                    Frame_Type = ''
                try:
                    Content = params['İçerik']
                except Exception as e:
                    Content = ''
                try:
                    Intended_Use = params['Kullanım Amacı']
                except Exception as e:
                    Intended_Use = ''
                try:
                    Heat_Technology = params['Isı Teknolojisi']
                except Exception as e:
                    Heat_Technology = ''
                try:
                    Container = params['Kap']
                except Exception as e:
                    Container = ''
                try:
                    Hanger = params['Askı']
                except Exception as e:
                    Hanger = ''
                try:
                    Top_Silhouette = params['Üst Siluet']
                except Exception as e:
                    Top_Silhouette = ''
                try:
                    Volume = params['Hacim']
                except Exception as e:
                    Volume = ''
                try:
                    Laptop_Bag_Size = params['Laptop Çantası Boyutu']
                except Exception as e:
                    Laptop_Bag_Size = ''
                try:
                    Dimension_Size_bag = params['Boyut/Ebat']
                except Exception as e:
                    Dimension_Size_bag = ''

                items.append(
                    [name, main_category, under_category, last_category, brand, wear_size, images, shoe_size, price,
                     sizes, url, sex, article, color, out_material, goal, Advantage, Binding, Outsole, material, form,
                     complect, collection, Arm_Type, Fabric_Type, style, Fabric_Technology, Size_Dimension,
                     Product_Type, Arm_Length, Thickness, size, Ambient, Number_of_Parts, Persona, back_size, Base_Type,
                     Heel_Type, Feature, Fabric_Feature, Leg_Type, Leg_Length, Waist, Type, School, Pattern, Capacity,
                     Sport_Branch, Closing_Shape, Collar_Type, Model, Cutting, Sport_Type, Liner_Condition,
                     Sustainability_Detail, Upper_Material, Heel_Height, Insole_Material, Lining_Material,
                     Leather_Quality, Additional_Feature, Filler, Sustainable, Pocket_Type, Pocket, Floor, Nail_Type,
                     Variety, Wrist_Style, Product_Details, Cord_Status, Silhouette, Bag_size, Yarn_Feature, Technical,
                     Bottom_Upper_Team, Belt, Shoe_Sole, Sole_Material, Pocket_Number, Filling_Technique,
                     Filling_Material, Branch, Weaving_Type, Printing_Technique, Equalization, Glass_Material,
                     Frame_Material, Glass_Type, Frame_Form, Glass_Color, Frame_Color, Frame_Type, Content,
                     Intended_Use, Heat_Technology, Container, Hanger, Top_Silhouette, Volume, Laptop_Bag_Size,
                     Dimension_Size_bag])
            except Exception as e:
                continue

        return items

    def save(self, data, file_name):
        columns = ['name', 'main_category', 'under_category', 'last_category', 'brand', 'wear_size', 'images',
                   'shoe_size',
                   'price', 'sizes', 'url', 'sex', 'article', 'color', 'out_material', 'goal', 'Advantage', 'Binding',
                   'Outsole', 'material', 'form', 'complect', 'collection', 'Arm_Type', 'Fabric_Type', 'style',
                   'Fabric_Technology', 'Size_Dimension', 'Product_Type', 'Arm_Length', 'Thickness', 'size', 'Ambient',
                   'Number_of_Parts', 'Persona', 'back_size', 'Base_Type', 'Heel_Type', 'Feature', 'Fabric_Feature',
                   'Leg_Type',
                   'Leg_Length', 'Waist', 'Type', 'School', 'Pattern', 'Capacity', 'Sport_Branch', 'Closing_Shape',
                   'Collar_Type', 'Model', 'Cutting', 'Sport_Type', 'Liner_Condition', 'Sustainability_Detail',
                   'Upper_Material', 'Heel_Height', 'Insole_Material', 'Lining_Material', 'Leather_Quality',
                   'Additional_Feature', 'Filler', 'Sustainable', 'Pocket_Type', 'Pocket', 'Floor', 'Nail_Type',
                   'Variety',
                   'Wrist_Style', 'Product_Details', 'Cord_Status', 'Silhouette', 'Bag_size', 'Yarn_Feature',
                   'Technical',
                   'Bottom_Upper_Team', 'Belt', 'Shoe_Sole', 'Sole_Material', 'Pocket_Number', 'Filling_Technique',
                   'Filling_Material', 'Branch', 'Weaving_Type', 'Printing_Technique', 'Equalization', 'Glass_Material',
                   'Frame_Material', 'Glass_Type', 'Frame_Form', 'Glass_Color', 'Frame_Color', 'Frame_Type', 'Content',
                   'Intended_Use', 'Heat_Technology', 'Container', 'Hanger', 'Top_Silhouette', 'Volume',
                   'Laptop_Bag_Size',
                   'Dimension_Size_bag']

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(fr'data/{file_name}.csv', index=False)

    def run(self):
        ids = self.get_all_item_id()
        data = self.get_data(ids)
        self.save(data, self.name_brand)
        print(f'{self.name_brand} completed')
