## Práctica 0702

* Ya que la práctica contiene el mismo módulo de la práctica anterior añadiré el contenido nuevo.

* controllers.py:

```python
@http.route('/api/subscription', type="http", methods=['GET'], csrf=False)
    def get_subscriptions(self):
        try:
            estados = request.params.get('status')
            estados_validos = ['active', 'inactive', 'pending', 'canceled']
            if estados_validos not in estados_validos:
                return request.make_response(
                    json.dumps({'error': 'Invalid status value. Allowed values are: ' + ', '.join(estados_validos)}),
                    headers={'application/json'},
                    status=400
                )
            status = [('status', '=', estados)] if estados else []
            subs = request.env['subscription.management'].search(status)
            if not subs:
                return request.make_response(
                    json.dumps({'msg': 'No subscriptions found'}),
                    headers={'Content-Type': 'application/json'},
                    status=404
                )
            resultado = [{'name': sub.name, 'status': sub.status} for sub in subs]
            return request.make_response(
                json.dumps({'subscriptions': resultado}),
                headers={'application/json'},
                status=200
            )
        except Exception as e:
            return request.make_response(
            json.dumps({'msg': f'Internal server error: {str(e)}'}),
            headers={'application/json'},
            status=500
        )
    
    @http.route('/api/subscription/<string:name>', auth='user', methods=['GET'], type='http')
    def get_subscription_by_name(self, name, **kwargs):
        try:
            subscription = request.env['subscription.management'].search(
                [('name', '=', name)],
                limit=1
            )

            if not subscription:
                return Response(
                    json.dumps({'error': 'Suscripción no encontrada'}),
                    status=404,
                    content_type='application/json'
                )

            subscription_data = subscription.read()[0]

            if subscription.customer_id:
                subscription_data['customer'] = {
                    'id': subscription.customer_id.id,
                    'name': subscription.customer_id.name
                }

            if subscription.usage_limit > 0:
                subscription_data['use_percent'] = min(
                    (subscription.current_usage / subscription.usage_limit) * 100,
                    100
                )

            return Response(
                json.dumps(subscription_data, default=str),
                status=200,
                content_type='application/json'
            )

        except Exception as e:
            return Response(
                json.dumps({'error': str(e)}),
                status=500,
                content_type='application/json'
            )
```