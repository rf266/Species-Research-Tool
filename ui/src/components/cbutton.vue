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
}
</style>