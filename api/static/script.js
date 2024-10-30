// script.js

// Инициализация карты с центром между Музеем и Гостиницей
const map = L.map('map').setView([42.4605, 59.6075], 16);

// Подключение карты OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Координаты точек
const museumCoords = [42.463311, 59.609948];
const hotelCoords = [42.457680, 59.605052];

// Маркеры для музея и гостиницы
L.marker(museumCoords).addTo(map)
    .bindPopup('Музей имени Савицкого')
    .openPopup();

L.marker(hotelCoords).addTo(map)
    .bindPopup('Гостиница "Ташкент"');

// Добавление маршрута (полилиния) между двумя точками
const route = [museumCoords, hotelCoords];
L.polyline(route, { color: 'blue', weight: 4, opacity: 0.7 }).addTo(map);
