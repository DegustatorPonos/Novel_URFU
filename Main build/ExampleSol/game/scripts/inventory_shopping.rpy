init python:
    class Inventory(object):
        def __init__(self):
            self.money = 0
            self.minigame_money = 0
            self.items = {}
            self.item_history = set()
            self.buy_history = set()
            renpy.log("inventory")
        
        def add_money(self, quantity, tag = None, minigame = False):
            if not getattr(self, 'add_money_tags', False):
                self.add_money_tags = []
            
            if tag and tag in self.add_money_tags:
                return
            
            if minigame and quantity > 0:
                self.minigame_money += quantity
            
            if tag:
                self.add_money_tags.append(tag)
            
            self.money += quantity
            
            if self.money_limit():
                self.money = min(self.money_limit(), self.money)
            
            return
        
        def money_limit(self):
            return 9999
        
        def buy(self, item, after_buy_label):
            self.money -= item["price"]
            
            id = item["id"]
            
            self.add_item(item)
            
            self.buy_history.add(id)
            
            if item["action_on_buy"]:
                eval(item["action_on_buy"])
            
            if item["label_on_buy"]:
                renpy.call( item["label_on_buy"], after_buy_label = after_buy_label)
            
            return
        
        def money_string(self):
            return "$" + str(self.money)
        
        def num_items(self, item):
            id = item["id"]
            return self.num_items_by_id(id)
        
        def num_items_by_id(self, id):
            if id in self.items:
                return self.items[id]
            else:
                return 0
            
            return
        
        def add_item(self, item, quantity = 1):
            id = item["id"]
            self.add_item_by_id(id, quantity)
            
            return
        
        def add_item_by_id(self, id, quantity = 1):
            if id in self.items:
                self.items[id] += quantity
            else:
                self.items[id] = quantity
            
            if quantity > 0:
                self.item_history.add(id)
            
            return
        
        def has_had_item_before(self, id):
            return id in self.item_history
        
        def has_bought_item_before(self, id):
            return id in self.buy_history
        
        def has_item(self, id):
            return id in self.items.keys()

    def buy_item_price(item):
        limit = item["limit"]
        
        if limit:
            if store.inventory.num_items_by_id(item["id"]) >= item["limit"]:
                if limit == 1:
                    limit_text = "Куплено!"
                else:
                    limit_text = "Распродано!"
                
                return "{color=" + gui.accent_color + "}" + limit_text + "{/color}"
        
        
        price_string = ""
        price = item["price"]
        
        if price > store.inventory.money:
            price_string += "{color=#ff0000}"
        
        price_string += "$" + str(price)
        
        if price > store.inventory.money:
            price_string += "{/color}"
        
        return price_string

    def buy_item_enabled(item):
        id = item["id"]
        
        if eval( item["condition_enabled"] ) == False:
            return False
        
        if item["price"] > inventory.money:
            return False
        
        if eval( item["disable_after_first_buy"] ) and store.inventory.has_bought_item_before(id):
            return False
        
        return True

    def buy_item_visible(item):
        id = item["id"]
        
        if id < 1:
            return False
        
        if eval( item["condition_visible"] ) == False:
            return False
        
        if eval( item["disappear_after_first_buy"] ) and store.inventory.has_bought_item_before(id):
            return False
        
        limit = item["limit"]
        
        if limit:
            if store.inventory.num_items_by_id(item["id"]) >= item["limit"]:
                return False
        
        return True

    def items_from_ids(item_ids):
        items = []
        
        for id in item_ids:
            item = store.database_items[id]
            items.append(item)
        
        return items

    def items_with_tag(tag):
        items = []
        
        for item in store.database_items:
            if item["id"] >= 1 and tag in item["tags"]:
                items.append(item)
        
        return items

    def visible_items_with_tag(tag):
        items = items_with_tag(tag)
        
        return [item for item in items if eval( item["condition_visible"] )]

label buy_menu(item_ids, back_label, after_buy_label):
    call screen buy_menu(item_ids, back_label, after_buy_label)
    return

screen buy_items(buy_menu_items, back_label, after_buy_label):
    vbox:
        xalign 0.5
        yalign 0.5

        hbox:
            spacing 50
            vbox:
                null width 1000
                text "Название"
                for buy_menu_item in buy_menu_items:
                    textbutton buy_menu_item["name"] action If(buy_item_enabled(buy_menu_item), Function(inventory.buy, buy_menu_item, after_buy_label), None)
                    if buy_menu_item["description"]:
                        text "{i}" + buy_menu_item["description"] + "{/i}"
                    null height 20

            vbox:
                null width 125
                text "Цена" xalign 0.5
                for buy_menu_item in buy_menu_items:
                    text buy_item_price(buy_menu_item) xalign 0.5
                    if buy_menu_item["description"]:
                        null height 75
                    else:
                        null height 25


            vbox:
                null width 125
                text "В Инвернтаре"
                for buy_menu_item in buy_menu_items:
                    text str(inventory.num_items(buy_menu_item)) xalign 0.5
                    if buy_menu_item["description"]:
                        null height 75
                    else:
                        null height 25


screen buy_menu(buy_menu_items, back_label, after_buy_label):
    default buy_screen_page = 1

    add "images/interface/ShoppingMenuBox.png" xalign 0.5 yalign 0.5

    $ buy_screen_page_amount = int( math.ceil(len(buy_menu_items) / float(5)) )

    $ buy_screen_page = min( buy_screen_page, buy_screen_page_amount )

    $ buy_screen_item_start_index = 0 + (5 * (buy_screen_page - 1) )
    $ buy_screen_item_end_index = 5 + (5 * (buy_screen_page - 1) )

    vbox:
        xalign 0.5 yalign 0.5
        use buy_items(buy_menu_items[buy_screen_item_start_index : buy_screen_item_end_index], back_label, after_buy_label)

    if buy_screen_page_amount > 1:
        vbox:
            xalign 0.5
            yalign 0.95

            text "Стр." size 64 xalign 0.5
            hbox:

                spacing gui.page_spacing

                textbutton "<" action If(buy_screen_page > 1, SetScreenVariable("buy_screen_page", buy_screen_page - 1), None) text_size 64

                for page in range(1, buy_screen_page_amount + 1):
                    textbutton "[page]" action SetScreenVariable("buy_screen_page", page) text_size 64

                textbutton ">" action If(buy_screen_page < buy_screen_page_amount, SetScreenVariable("buy_screen_page", buy_screen_page + 1), None) text_size 64

    use back_button(click_action=Jump(back_label), xalign=0.98, yalign=0.98)

label buy_process_response_end(after_buy_label):
    call character_leave_dissolve (n)
    call clear_and_reset_characters
    $ renpy.pause(0.5)
    $ renpy.call(after_buy_label)

    return