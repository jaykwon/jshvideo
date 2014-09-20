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
      },
      getVideo: function(videoId) {
          return $http.get('/data/' + videoId + '.json')
            .success(function(result) {
                return result;
            });
      }
  };
});

app.controller('HomeController', ['$scope', '_', 'videoFactory', function ($scope, _, videoFactory) {
  $scope.hello = videoFactory.sayHello('World');
  videoFactory.getVideos().then(function(videos) {
      console.log(videos);
      $scope.videos = videos.data;
  });
  $scope.openVex = function(clickEvent) {
      vex.dialog.alert({
          message: _.template()
      });
  };
}]);

app.controller('DetailController', ['$scope', '$routeParams', 'videoFactory', function($scope, $routeParams, videoFactory) {
    $scope.id = $routeParams.id;
    videoFactory.getVideo($routeParams.id).then(function(video) {
        console.log(video);
        $scope.video = video.data;
        $scope.videoLink = '/media/videos/' + video.data.basename;
        console.log("src:", $scope.videoLink, "type:", $scope.video.mime_type.text);
        $scope.videoPlaylist = [
            {
              src: 'media/videos/mnm.webm',
              type: 'video/webm'
            }
        ]
    });
}]);
