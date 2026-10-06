import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildSteps.maven

version = "2024.12"

project {
    buildType(Build)
}

object Build : BuildType({
    name = "Build, test, package"
    steps {
        maven { goals = "compile" }
        maven { goals = "verify" }
        maven { goals = "-DskipTests package" }
    }
})
