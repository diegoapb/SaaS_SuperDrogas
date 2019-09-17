$(document).ready(() => {
  let btns = document.getElementsByClassName('btn-agregar');
  for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", addRowList);
  }

  document.getElementById('btn-facturar').addEventListener('click', (e) => {
    document.getElementById('modal-suma-restante').value = document.getElementById('btn-facturar').innerHTML;
    document.getElementById('modal-entregado').value = document.getElementById('btn-facturar').innerHTML;
  });
});

const addRowList = (e) => {
  let data = e.target.parentNode.parentNode;
  let cantidad = data.getElementsByTagName('input')[0].value;
  let tdNombre = createCustomElement('td', {}, [data.dataset.nombre]);
  let tdPrecio = createCustomElement('td', {}, [`$${data.dataset.precio}`]);
  let tdCantidad = createCustomElement('td', {}, [cantidad]);
  let subtotal = cantidad * data.dataset.precio;
  let tdSubtotal = createCustomElement('td', {}, [`$${subtotal}`]);
  let btnEliminar = createCustomElement('button', {
    'type': 'button',
    'class': 'btn btn-primary',
  }, ['X']);
  btnEliminar.addEventListener('click', deleteRowList);
  let tdEliminar = createCustomElement('td', {}, [btnEliminar]);
  let tr = createCustomElement('tr', {
    'data-id': data.dataset.id,
    'data-cantidad': cantidad,
    'data-subtotal': subtotal,
  }, [tdNombre, tdPrecio, tdCantidad, tdSubtotal, tdEliminar]);
  document.getElementById('tbodyVentas').appendChild(tr);

  // Agregamos el valor total al botón
  let valorTotal = parseInt(document.getElementById('btn-facturar').innerHTML.slice(1));
  valorTotal += subtotal;
  document.getElementById('btn-facturar').innerHTML = `$${valorTotal}`;
  document.getElementById('btn-facturar').setAttribute('data-toggle', 'modal')
  document.getElementById('btn-facturar').setAttribute('data-target', '#facturarModal')
}

const deleteRowList = (e) => {
  let data = e.target.parentNode.parentNode; // This is the tr tag
  let valorTotal = parseInt(document.getElementById('btn-facturar').innerHTML.slice(1));
  valorTotal -= data.dataset.subtotal;
  document.getElementById('btn-facturar').innerHTML = `$${valorTotal}`;
  if (valorTotal == 0) {
    document.getElementById('btn-facturar').removeAttribute('data-toggle')
    document.getElementById('btn-facturar').removeAttribute('data-target')
  }

  // Removing the tr tag
  data.parentNode.removeChild(data);
}

function createCustomElement(element, attributes, children) {
  let customElement = document.createElement(element);
  if (children !== undefined) {
    children.forEach(function(el) {
      if (el.nodeType) {
        if (el.nodeType === 1 || el.nodeType === 11) customElement.appendChild(el);
      } else {
        customElement.innerHTML += el;
      }
    });
  }
  addAttributes(customElement, attributes);
  return customElement;
}

function addAttributes(element, attrObj) {
  for (let attr in attrObj) {
    if (attrObj.hasOwnProperty(attr)) element.setAttribute(attr, attrObj[attr])
  }
}
