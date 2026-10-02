from datetime import datetime
Kello = datetime.now().hour
if (Kello <= 7):
    print("Vielä voi jatkaa unia.") 

elif (Kello <= 8): 
    print("Aika nousta luennolle.") 

elif (Kello <= 12):
    print("Nukuin pahasti pommiin, mutta vielä kerkeää iltapäivän opiskella.")

else:
    print("Tuli nukuttua pommista yli...") 
