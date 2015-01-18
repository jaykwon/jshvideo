// Declare app level module which depends on filters, and services
var app = angular.module('app', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date', 'underscore', "mediaPlayer", 'ngDisqus', 'satellizer'])
  .config(['$routeProvider', '$locationProvider', '$disqusProvider', '$authProvider', function ($routeProvider, $locationProvider, $disqusProvider, $authProvider) {
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
    $authProvider.twitter({
        url: '/auth/twitter'
    });
  }]);
