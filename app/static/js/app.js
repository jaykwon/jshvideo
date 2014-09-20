// Declare app level module which depends on filters, and services
var app = angular.module('app', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date', 'ngDisqus', 'underscore', 'mediaPlayer'])
  .config(['$routeProvider', '$locationProvider', '$disqusProvider', function ($routeProvider, $locationProvider, $disqusProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html',
        controller: 'HomeController'})
      .when('/videos/:id', {
        templateUrl: 'views/home/detail.html',
        controller: 'DetailController'})
      .otherwise({redirectTo: '/'});
    $locationProvider
      .html5Mode(false)
      .hashPrefix('!');
    $disqusProvider
      .setShortname('mightynorth');
;  }]);
