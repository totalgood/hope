// Gruntfile.js

// our wrapper function (required by grunt and its plugins)
// all configuration goes inside this function
module.exports = function(grunt) {

  // ===========================================================================
  // CONFIGURE GRUNT ===========================================================
  // ===========================================================================
  grunt.initConfig({

    // get the configuration info from package.json ----------------------------
    // this way we can use things like name and version (pkg.name)
    pkg: grunt.file.readJSON('package.json'),

    // configure jshint to validate js files -----------------------------------
    jshint: {
      options: {
        reporter: require('jshint-stylish') // use jshint-stylish to make our errors look and read good
      },

      // when this task is run, lint the Gruntfile and all js files in src
      build: ['Gruntfile.js', 'docs/**/*.js']
    },

    // configure uglify to minify js files -------------------------------------
    uglify: {
      options: {
        banner: '/*\n <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> \n*/\n'
      },
      build: {
        files: {
          'docs/slides/js/reveal.min.js': 'docs/slides/js/reveal.js',
          'docs/slides/css/reveal.min.css': 'docs/slides/css/reveal.css'
        }
      }
    },

    // compile less stylesheets to css -----------------------------------------
    less: {
      build: {
        files: {
          'dist/css/pretty.css': 'src/css/pretty.less'
        }
      }
    },

    // configure cssmin to minify css files ------------------------------------
    cssmin: {
      options: {
        banner: '/*\n <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> \n*/\n'
      },
      build: {
        files: {
          'docs/slides/css/reveal.min.css': 'docs/slides/css/reveal.css'
        }
      }
    },

    pandoc: {
    index.html: { // OUTPUT file name 
      configs: {
        "publish"   : 'html5',                 // Publish File Format. 
        "title"     : "Hope for Chatbots",        // EPUB Title 
        "stylesheet": "docs/css/revealjs.css"     // EPUB include StyleSheet File Path. 
        "filter"    : myFilterFunc            // Calling Before Execute Command. 
      },
      files: {
        "chapters": [
          "docs/slides/slides.md"
        ]
      }
    }
  }

  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');
};
