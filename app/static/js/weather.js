const appKey = "ff532977349290d86ac2bc3243a8ca5a";

var searchButton = document.getElementById("search-btn"),
  searchInput = document.getElementById("search-txt"),
  cityName = document.getElementById("city-name"),
  icon = document.getElementById("icon"),
  temperature = document.getElementById("temp"),
  humidity = document.getElementById("humidity-div"),
  forecastIcon = document.getElementById("forecast-icon"),
  forecastTemp = document.getElementById("forecast-temp"),
  forecastHumidity = document.getElementById("forecast-humidity");

searchButton.addEventListener("click", findWeatherDetails);
searchInput.addEventListener("keyup", enterPressed);

function enterPressed(event) {
  if (event.key === "Enter") {
    findWeatherDetails();
  }
}

function findWeatherDetails() {
  if (searchInput.value === "") {
    alert("Please enter a city name");
  } else {
    let searchLink = "https://api.openweathermap.org/data/2.5/weather?q=" + searchInput.value + "&appid=" + appKey;
    httpRequestAsync(searchLink, theResponse);

    let forecastLink = "https://api.openweathermap.org/data/2.5/forecast?q=" + searchInput.value + "&appid=" + appKey;
    httpRequestAsync(forecastLink, theForecastResponse);
  }
}

function theResponse(response) {
  let jsonObject = JSON.parse(response);
  cityName.innerHTML = jsonObject.name;
  icon.src = "http://openweathermap.org/img/w/" + jsonObject.weather[0].icon + ".png";
  temperature.innerHTML = parseInt(jsonObject.main.temp - 273) + "°C"; // Chuyển đổi từ Kelvin sang Celsius
  humidity.innerHTML = jsonObject.main.humidity + "%";
}

function theForecastResponse(response) {
  let jsonObject = JSON.parse(response);
  // Lấy dữ liệu dự báo cho ngày mai (24 giờ sau)
  let forecast = jsonObject.list.find(item => {
    let forecastDate = new Date(item.dt * 1000);
    let tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    return forecastDate.getDate() === tomorrow.getDate();
  });

  if (forecast) {
    forecastIcon.src = "http://openweathermap.org/img/w/" + forecast.weather[0].icon + ".png";
    forecastTemp.innerHTML = parseInt(forecast.main.temp - 273) + "°C"; // Chuyển đổi từ Kelvin sang Celsius
    forecastHumidity.innerHTML = forecast.main.humidity + "%";
  }
}

function httpRequestAsync(url, callback) {
  var httpRequest = new XMLHttpRequest();
  httpRequest.onreadystatechange = () => { 
      if (httpRequest.readyState == 4 && httpRequest.status == 200)
          callback(httpRequest.responseText);
  }
  httpRequest.open("GET", url, true); 
  httpRequest.send();
}

// Lấy dữ liệu thời tiết cho Hà Nội khi trang được tải
document.addEventListener('DOMContentLoaded', function() {
  const defaultCity = 'Hanoi';
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${defaultCity}&appid=${appKey}`;
  const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${defaultCity}&appid=${appKey}`;

  httpRequestAsync(url, theResponse);
  httpRequestAsync(forecastUrl, theForecastResponse);
});