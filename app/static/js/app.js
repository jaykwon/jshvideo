// Declare app level module which depends on filters, and services
var app = angular.module('app', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date', 'underscore', "mediaPlayer"])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html',
        controller: 'HomeController'})
      .when('/videos/:id', {
        templateUrl: 'views/home/detail.html',
        controller: 'DetailController'})
      .otherwise({redirectTo: '/'});
  }]);
