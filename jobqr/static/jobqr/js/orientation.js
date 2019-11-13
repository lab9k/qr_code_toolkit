const Orientation = (function orientation() {
  const self = {};

  const getOrientation = () => {
    const ori = screen.orientation.angle;
    const width = (ori === 90 || ori === -90) ? screen.width : screen.height;
    const height = (width === screen.width) ? screen.height : screen.width;
    return {width, height};
  };

  window.addEventListener('orientationchange', function () {
    self.dimensions = getOrientation();
  });

  self.dimensions = getOrientation();

  return self;
})();