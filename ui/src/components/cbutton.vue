<template>
    <button class="btn">
        <slot>
        Submit
        </slot>

    </button>
</template>

<style scoped>
.btn {
    background: beige;
    color: brown;
    border:color-mix(in xyz, red 20, brown 80);
    cursor: pointer;
    font-size: 20px;
    font-family:Georgia;
    font-weight: 100;
    border-radius: 15%;
    border-bottom-color: antiquewhite;

}
</style>
