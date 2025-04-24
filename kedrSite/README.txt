Все необходимые библиотеки для работы содержаться в файле requirements.txt
Чтобы их скачать нужно в терминале выполнить команду pip install -r requirements.txt
рекомендую это делать в виртуальной среде, чтобы после окончания проекта не париться с их очисткой со своего пк.

Чтобы запустить бэкенд-сервер, нужно выполнить команду manage.py runserver находясь в папке kedrSite.
все необходимые юрлы можно найти в файле kedSite.urls.py

По факту в проекте должна быть postgreSQL, но так как для налаживания свзяи фронта с бэком это  не важно,
для удобства я временно ее поменял на SQLite.

Также, это еще недоделанная версия бэка, тут вполне могут быть какие-то ошибки, не позволяющие нормально работать с
фронтом, если что, пиши мне.

Папка frontend не нужна и не используется, можешь на нее не обращать внимания
 энд-пойнты:
/djoser-auth/token/login/       djoser.views.TokenCreateView    login - вход
/djoser-auth/token/logout/      djoser.views.TokenDestroyView   logout - выход
/api/v1/trees/  trees.views.TreesAPIList        trees - все деревья со всеми данными
/api/v1/trees/<int:pk>/ trees.views.TreesAPIDetails     tree - одно дерево с данными о нем
/api/v1/trees_coordinates/      trees.views.TreesAPICoordinates trees coordinates - координаты всех деревьев
/api/v1/djoser-auth/users/      djoser.views.UserViewSet        customuser-list - на данный момент используется для регистрации


