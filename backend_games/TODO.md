# TODO List for Changing API from Cars to Video Games

- [x] Rename directory 'cars' to 'games'
- [ ] Rename media/car_images to media/game_images
- [x] Update models.py: Change Car to Game with fields title, year, price, developer, description, image
- [ ] Update serializers.py: Change CarSerializer to GameSerializer
- [x] Update views.py: Change CarViewSet to GameViewSet
- [ ] Update games/urls.py: Change router.register to 'games', CarViewSet to GameViewSet
- [ ] Update games/admin.py: Register Game instead of Car
- [ ] Update backend/settings.py: Change 'cars' to 'games' in INSTALLED_APPS
- [ ] Update backend/urls.py: Change include('cars.urls') to 'games.urls'
- [ ] Run python manage.py makemigrations games
- [ ] Run python manage.py migrate
