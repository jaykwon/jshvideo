var underscore = angular.module('underscore', []);
underscore.factory('_', function() {
  return window._; // assumes underscore has already been loaded on the page
});

app.factory('videoFactory', function ($http) {
  return {
      getVideos: function() {
          return $http.get('/data/test_data.json')
            .success(function(result) {
                return result;
            });
      },
      sayHello: function(name) {
          return "Hello " + name + "!";
      }
  };
});

app.controller('HomeController', ['$scope', '_', 'videoFactory', function ($scope, _, videoFactory) {
  $scope.tests =  ['one', 'two', 'three'];
  //videoFactory.sayHello('World');
  $scope.hello = videoFactory.sayHello('World');
  videoFactory.getVideos().then(function(videos) {
      console.log(videos);
      $scope.videos = videos.data;
  });
}]);
