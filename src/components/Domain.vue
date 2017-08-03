<template lang="pug">
  div(class="Main")
    header(data-role="header" data-position="fixed")
      div(class="brandzone")
        a(href="https://www.yandex.ru/" class="brand-logo") Гланис
          img(class = "logo" src = "../assets/logo_blue.png")
          img(class = "logo" v-if = "false" src = "@/assets/logo_red.png")
          img(class = "logo" v-if = "false" src = "@/assets/logo_blue.png")

        input(type="text" placeholder="Категория или товар…" autofocus)

    h2(v-for = "d in parts") {{d.data}}
      h6(v-for = "c in d.children") {{c}}


</template>

<script lang="coffee">
export default
  name: 'Main'
  data: ->
    msg: 'Welcome to Your Vue.js App'
    parts:[
      {
        "data": "Больницы"
        "children": [
          "Реанимация"
          "Хирургия"
        ]
      }

      {
        "data": "Поликлиники"
        "children": [
          "Кардиологя"
          "Терапия"
        ]
      }
    ]


</script>

<style lang="sass" scoped>
  $btfl_blue: #56CCF2

  *
    font-family: Arial
  a
    color: black
    text-decoration: none

  body
    margin: 0 5%
    display: flex
    flex-direction: column
    align-items: flex-start

  header
    margin-left: -5%
    padding: .3em 0 .3em 5%
    z-index: 100
    position: fixed
    display: flex
    align-items: flex-start
    width: 100%
    background-color: white
    border-bottom: .3em solid $btfl_blue

    .brandzone
      display: flex
      align-items: center

      .brand-logo
        display: flex
        justify-content: space-between
        font: 22pt Segoe UI Semibold

        .logo
          margin-left: .4em
          width: 43px
          height: 40px

        &:hover
          opacity: .3

      .domain
        margin-left: .3em
        font: 1.2em Segoe UI
        &:hover
          opacity: .3


    input
      outline: none !important
      margin:  auto 1em
      border: solid 1px black
      border-radius: 30px
      height: 2.5em
      padding-left: 1em
      width: 50%
</style>
