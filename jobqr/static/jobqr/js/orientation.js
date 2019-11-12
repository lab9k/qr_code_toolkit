const Orientation = (function orientation() {
  const self = {};

  const getOrientation = () => {
    const ori = screen.orientation.angle;
    const width = screen.width;
    const height = screen.height;
    console.log({width, height, ori, sWidth: screen.width, sHeight: screen.height});
    return {width, height};
  };

  window.addEventListener('orientationchange', function () {
    self.dimensions = getOrientation();
  });

  self.dimensions = getOrientation();

  return self;
})();