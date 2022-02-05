
cities= ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Bihar"]
city_short ={
    "Mumbai": "Mum",
    "Delhi" : "Del",
    "Bangalore" : "Blr",
    "Kolkata" : "Kol",
    "Bihar" : "Bhr"
}
for index in range(len(cities)):
    print(index)
    print(cities[index])
    #print(city_short.get(cities[index]))