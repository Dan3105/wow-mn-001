<!-- From Uiverse.io by andrew-demchenk0 --> 
<button class="button">
  <svg fill="none" height="24" viewBox="0 0 24 24" width="24" class="svg-icon">
    <g
      clip-rule="evenodd"
      fill-rule="evenodd"
      stroke="#056dfa"
      stroke-linecap="round"
      stroke-width="2"
    >
      <path
        d="m3 7h17c.5523 0 1 .44772 1 1v11c0 .5523-.4477 1-1 1h-16c-.55228 0-1-.4477-1-1z"
      ></path>
      <path
        d="m3 4.5c0-.27614.22386-.5.5-.5h6.29289c.13261 0 .25981.05268.35351.14645l2.8536 2.85355h-10z"
      ></path>
    </g>
  </svg>
  <span class="lable">Archive</span>
</button>

<style>
/* From Uiverse.io by andrew-demchenk0 */ 
.button {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 12px 8px 16px;
  gap: 8px;
  height: 40px;
  width: 128px;
  border: none;
  background: #056bfa27;
  border-radius: 20px;
  cursor: pointer;
}

.lable {
  margin-top: 1px;
  font-size: 19px;
  line-height: 22px;
  color: #056dfa;
  letter-spacing: 1px;
}

.button:hover {
  background: #056bfa49;
}

.button:hover .svg-icon {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  25% {
    transform: rotate(-8deg);
  }

  50% {
    transform: rotate(0deg);
  }

  75% {
    transform: rotate(8deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

</style>