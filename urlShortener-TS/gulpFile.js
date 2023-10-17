// for typescript
const gulp = require('gulp');
const ts = require('gulp-typescript');
const tsProject = ts.createProject('tsconfig.json')

const { src, dest, watch, series} =  require ('gulp')


// compile ts 
function buildTs(){
    return gulp.src("./*.ts")
        .pipe(tsProject())
        .js.pipe(dest('./jsFile'))
}

function watchTask() {
    watch(['./*.ts'], buildTs)
}

exports.default = series(buildTs, watchTask)