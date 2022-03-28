(function (t) {
  function e(e) {
    for (
      var a, o, r = e[0], c = e[1], l = e[2], u = 0, m = [];
      u < r.length;
      u++
    )
      (o = r[u]),
        Object.prototype.hasOwnProperty.call(s, o) && s[o] && m.push(s[o][0]),
        (s[o] = 0);
    for (a in c) Object.prototype.hasOwnProperty.call(c, a) && (t[a] = c[a]);
    d && d(e);
    while (m.length) m.shift()();
    return n.push.apply(n, l || []), i();
  }
  function i() {
    for (var t, e = 0; e < n.length; e++) {
      for (var i = n[e], a = !0, r = 1; r < i.length; r++) {
        var c = i[r];
        0 !== s[c] && (a = !1);
      }
      a && (n.splice(e--, 1), (t = o((o.s = i[0]))));
    }
    return t;
  }
  var a = {},
    s = { risk: 0 },
    n = [];
  function o(e) {
    if (a[e]) return a[e].exports;
    var i = (a[e] = { i: e, l: !1, exports: {} });
    return t[e].call(i.exports, i, i.exports, o), (i.l = !0), i.exports;
  }
  (o.m = t),
    (o.c = a),
    (o.d = function (t, e, i) {
      o.o(t, e) || Object.defineProperty(t, e, { enumerable: !0, get: i });
    }),
    (o.r = function (t) {
      'undefined' !== typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(t, Symbol.toStringTag, { value: 'Module' }),
        Object.defineProperty(t, '__esModule', { value: !0 });
    }),
    (o.t = function (t, e) {
      if ((1 & e && (t = o(t)), 8 & e)) return t;
      if (4 & e && 'object' === typeof t && t && t.__esModule) return t;
      var i = Object.create(null);
      if (
        (o.r(i),
        Object.defineProperty(i, 'default', { enumerable: !0, value: t }),
        2 & e && 'string' != typeof t)
      )
        for (var a in t)
          o.d(
            i,
            a,
            function (e) {
              return t[e];
            }.bind(null, a)
          );
      return i;
    }),
    (o.n = function (t) {
      var e =
        t && t.__esModule
          ? function () {
              return t['default'];
            }
          : function () {
              return t;
            };
      return o.d(e, 'a', e), e;
    }),
    (o.o = function (t, e) {
      return Object.prototype.hasOwnProperty.call(t, e);
    }),
    (o.p = '');
  var r = (window['webpackJsonp'] = window['webpackJsonp'] || []),
    c = r.push.bind(r);
  (r.push = e), (r = r.slice());
  for (var l = 0; l < r.length; l++) e(r[l]);
  var d = c;
  n.push([1, 'chunk-vendors']), i();
})({
  '063a': function (t, e, i) {
    function a() {
      $('.tips-box .title span').text('提示信息'),
        $('.tips-content').text('查询失败，请稍后重试！'),
        $('.tips-bg').show();
    }
    function s(t) {
      var e = (new Date().getTime() / 1e3).toFixed(),
        i = '23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA',
        a = '123456789abcdefg',
        s = 'zdww';
      return JSON.stringify(
        Object.assign(
          {
            appId: 'NcApplication',
            paasHeader: s,
            timestampHeader: e,
            nonceHeader: a,
            signatureHeader: CryptoJS.SHA256(e + i + a + e)
              .toString(CryptoJS.enc.Hex)
              .toUpperCase(),
          },
          t
        )
      );
    }
    function n(t, e) {
      var i = s(t),
        n = JSON.parse(i).timestampHeader,
        o = CryptoJS.SHA256(
          n + 'fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA' + n
        )
          .toString(CryptoJS.enc.Hex)
          .toUpperCase();
      return $.ajax(
        Object.assign(
          {
            headers: {
              'x-wif-nonce': 'QkjjtiLM2dCratiA',
              'x-wif-paasid': 'smt-application',
              'x-wif-signature': o,
              'x-wif-timestamp': n,
            },
            url: 'https://bmfw.www.gov.cn/bjww/interface/interfaceJson',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            crossDomain: !0 === !document.all,
            data: i,
          },
          {
            headers: {
              'x-wif-nonce': 'QkjjtiLM2dCratiA',
              'x-wif-paasid': 'smt-application',
              'x-wif-signature': o,
              'x-wif-timestamp': n,
            },
          },
          e
        )
      )
        .then(function (t) {
          if (0 !== t.code) throw t;
          return t;
        })
        .catch(function (t) {
          a(),
            $('.closed').on('click', function () {
              $('.tips-bg').hide();
            });
        })
        .always(function () {
          $('.loading').hide();
        });
    }
    i('b680'), i('d3b7'), i('25f0'), (window.Ajax = n);
  },
  '06ca': function (t, e, i) {},
  1: function (t, e, i) {
    t.exports = i('cafc');
  },
  '4c92': function (t, e, i) {
    t.exports = i.p + 'source/PC/img/ali-erweima.a29de7c0.jpg';
  },
  '5df0': function (t, e, i) {
    'use strict';
    var a = i('06ca'),
      s = i.n(a);
    s.a;
  },
  '70bf': function (t, e, i) {
    t.exports = i.p + 'source/PC/img/wx-erweima.377ccccd.png';
  },
  cafc: function (t, e, i) {
    'use strict';
    i.r(e);
    i('e623'), i('e379'), i('5dc8'), i('37e1'), i('db4d');
    var a = i('2b0e'),
      s = function () {
        var t = this,
          e = t.$createElement,
          i = t._self._c || e;
        return i('div', [
          i('div', { staticClass: 'r-header' }, [
            i('p', { staticClass: 'r-time' }, [
              t._v('截至' + t._s(t.end_update_time) + '，全国疫情：'),
            ]),
            i(
              'div',
              {
                staticClass: 'r-high',
                class: { active: 'high' === t.activeName },
                on: {
                  click: function (e) {
                    t.activeName = 'high';
                  },
                },
              },
              [
                t._v(' 高风险等级地区'),
                i('span', [t._v('（' + t._s(t.hcount) + '）')]),
              ]
            ),
            i(
              'div',
              {
                staticClass: 'r-middle',
                class: { active: 'middle' === t.activeName },
                on: {
                  click: function (e) {
                    t.activeName = 'middle';
                  },
                },
              },
              [
                t._v(' 中风险等级地区'),
                i('span', [t._v('（' + t._s(t.mcount) + '）')]),
              ]
            ),
          ]),
          i(
            'div',
            {
              directives: [
                {
                  name: 'show',
                  rawName: 'v-show',
                  value: 'high' === t.activeName,
                  expression: "activeName === 'high'",
                },
              ],
              staticClass: 'h-content',
            },
            [
              i(
                'div',
                { staticClass: 'h-container' },
                [
                  t._l(t.highPageSlice, function (e, a) {
                    return [
                      i('div', { key: a, staticClass: 'h-header' }, [
                        t._v(' ' + t._s(e.area_name) + ' '),
                        i(
                          'span',
                          {
                            directives: [
                              {
                                name: 'show',
                                rawName: 'v-show',
                                value: !e.communitys.length,
                                expression: '!li.communitys.length',
                              },
                            ],
                            staticClass: 'h-span',
                            staticStyle: { color: '#F26161' },
                          },
                          [t._v(' 高风险 ')]
                        ),
                        i(
                          'table',
                          {
                            directives: [
                              {
                                name: 'show',
                                rawName: 'v-show',
                                value: e.communitys.length,
                                expression: 'li.communitys.length',
                              },
                            ],
                            key: 'table' + a,
                            staticClass: 'h-table',
                          },
                          t._l(e.communitys, function (e, a) {
                            return i(
                              'tr',
                              {
                                key: a,
                                staticClass: 'h-tr',
                                class: a % 2 === 0 ? 'even' : 'odd',
                              },
                              [
                                i('td', { staticClass: 'h-td1' }, [
                                  t._v(t._s(e)),
                                ]),
                                i(
                                  'td',
                                  {
                                    staticClass: 'h-td2',
                                    staticStyle: {
                                      color: '#F26161',
                                      'font-weight': 'bold',
                                    },
                                  },
                                  [t._v('高风险')]
                                ),
                              ]
                            );
                          }),
                          0
                        ),
                      ]),
                    ];
                  }),
                  i(
                    'div',
                    {
                      directives: [
                        {
                          name: 'show',
                          rawName: 'v-show',
                          value: !t.highlist.length && t.loaded,
                          expression: '!highlist.length && loaded',
                        },
                      ],
                      staticClass: 'nodata',
                    },
                    [
                      t._m(0),
                      i(
                        'div',
                        {
                          staticStyle: {
                            'font-size': '14px',
                            color: '#666',
                            float: 'right',
                            'font-weight': 'normal',
                          },
                        },
                        [t._v(' 有关信息来自当地上报的疫情风险等级 ')]
                      ),
                    ]
                  ),
                ],
                2
              ),
              i(
                'div',
                {
                  directives: [
                    {
                      name: 'show',
                      rawName: 'v-show',
                      value: t.highlist.length && t.loaded,
                      expression: 'highlist.length && loaded',
                    },
                  ],
                  staticClass: 'bottom-text',
                },
                [
                  i('div', { ref: 'page', staticClass: 'pages-box' }),
                  t._m(1),
                  i('div', { staticClass: 'source' }, [
                    t._v(' 有关信息来自当地上报的疫情风险等级 '),
                  ]),
                ]
              ),
            ]
          ),
          i(
            'div',
            {
              directives: [
                {
                  name: 'show',
                  rawName: 'v-show',
                  value: 'middle' === t.activeName,
                  expression: "activeName === 'middle'",
                },
              ],
              staticClass: 'm-content',
            },
            [
              i(
                'div',
                { staticClass: 'm-container' },
                [
                  t._l(t.middlePageSlice, function (e, a) {
                    return [
                      i('div', { key: a, staticClass: 'm-header' }, [
                        t._v(' ' + t._s(e.area_name) + ' '),
                        i(
                          'span',
                          {
                            directives: [
                              {
                                name: 'show',
                                rawName: 'v-show',
                                value: !e.communitys.length,
                                expression: '!li.communitys.length',
                              },
                            ],
                            staticClass: 'm-span',
                            staticStyle: { color: '#FDBE34' },
                          },
                          [t._v(' 中风险 ')]
                        ),
                        i(
                          'table',
                          {
                            directives: [
                              {
                                name: 'show',
                                rawName: 'v-show',
                                value: e.communitys.length,
                                expression: 'li.communitys.length',
                              },
                            ],
                            key: 'table' + a,
                            staticClass: 'm-table',
                          },
                          t._l(e.communitys, function (e, a) {
                            return i(
                              'tr',
                              {
                                key: a,
                                staticClass: 'm-tr',
                                class: a % 2 === 0 ? 'even' : 'odd',
                              },
                              [
                                i('td', { staticClass: 'm-td1' }, [
                                  t._v(t._s(e)),
                                ]),
                                i(
                                  'td',
                                  {
                                    staticClass: 'm-td2',
                                    staticStyle: {
                                      color: '#FDBE34',
                                      'font-weight': 'bold',
                                    },
                                  },
                                  [t._v('中风险')]
                                ),
                              ]
                            );
                          }),
                          0
                        ),
                      ]),
                    ];
                  }),
                  i(
                    'div',
                    {
                      directives: [
                        {
                          name: 'show',
                          rawName: 'v-show',
                          value: !t.middlelist.length && t.loaded,
                          expression: '!middlelist.length && loaded',
                        },
                      ],
                      staticClass: 'nodata',
                    },
                    [
                      t._m(2),
                      i(
                        'div',
                        {
                          staticStyle: {
                            'font-size': '14px',
                            color: '#666',
                            float: 'right',
                            'font-weight': 'normal',
                          },
                        },
                        [t._v(' 有关信息来自当地上报的疫情风险等级 ')]
                      ),
                    ]
                  ),
                ],
                2
              ),
              i(
                'div',
                {
                  directives: [
                    {
                      name: 'show',
                      rawName: 'v-show',
                      value: t.middlelist.length && t.loaded,
                      expression: 'middlelist.length && loaded',
                    },
                  ],
                  staticClass: 'bottom-text',
                },
                [
                  i('div', { ref: 'page1', staticClass: 'pages-box' }),
                  t._m(3),
                  i('div', { staticClass: 'source' }, [
                    t._v(' 有关信息来自当地上报的疫情风险等级 '),
                  ]),
                ]
              ),
            ]
          ),
          t._m(4),
        ]);
      },
      n = [
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i('div', { staticClass: 'imgbox-dj' }, [
            i('img', {
              attrs: { src: 'source/PC/images/tit-noct.png', alt: '' },
            }),
            i('div', { staticClass: 'img-tit-dj' }, [
              t._v('暂无高风险等级地区'),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i('p', [
            t._v('注：其余未列出地区均为'),
            i(
              'span',
              {
                staticClass: 'low-risk',
                staticStyle: { 'font-weight': 'bold' },
              },
              [t._v('低风险')]
            ),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i('div', { staticClass: 'imgbox-dj' }, [
            i('img', {
              attrs: { src: 'source/PC/images/tit-noct.png', alt: '' },
            }),
            i('div', { staticClass: 'img-tit-dj' }, [
              t._v('暂无中风险等级地区'),
            ]),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            i = t._self._c || e;
          return i('p', [
            t._v('注：其余未列出地区均为'),
            i(
              'span',
              {
                staticClass: 'low-risk',
                staticStyle: { 'font-weight': 'bold' },
              },
              [t._v('低风险')]
            ),
          ]);
        },
        function () {
          var t = this,
            e = t.$createElement,
            a = t._self._c || e;
          return a('div', { staticClass: 'main-jycx' }, [
            a('div', { staticClass: 'erweimaBox' }, [
              a('div', { staticStyle: { 'margin-right': '50px' } }, [
                a('img', {
                  staticClass: 'erweima',
                  attrs: { src: i('70bf'), alt: '' },
                }),
                a('p', { staticClass: 'er-txt' }, [t._v('微信扫码查询')]),
              ]),
              a('div', [
                a('img', {
                  staticClass: 'erweima',
                  attrs: { src: i('4c92'), alt: '' },
                }),
                a('p', { staticClass: 'er-txt' }, [t._v('支付宝扫码查询')]),
              ]),
            ]),
            a('div', { staticClass: 'footer_depart' }, [
              a('p', [t._v('本服务由国家卫生健康委提供')]),
            ]),
          ]);
        },
      ],
      o = (i('fb6a'), i('4795'), i('96cf'), i('1da1')),
      r = {
        data: function () {
          return {
            end_update_time: '',
            hcount: '0',
            mcount: '0',
            activeName: 'high',
            highlist: [],
            middlelist: [],
            loaded: !1,
            page: 1,
            page1: 1,
          };
        },
        mounted: function () {
          this.ajaxGetCount();
        },
        computed: {
          highPageSlice: function () {
            var t = 10 * (this.page - 1),
              e = t + 10;
            return this.highlist.slice(t, e);
          },
          middlePageSlice: function () {
            var t = 10 * (this.page1 - 1),
              e = t + 10;
            return this.middlelist.slice(t, e);
          },
        },
        methods: {
          ajaxGetCount: function () {
            var t = this;
            return Object(o['a'])(
              regeneratorRuntime.mark(function e() {
                var i, a, s, n, o, r, c;
                return regeneratorRuntime.wrap(function (e) {
                  while (1)
                    switch ((e.prev = e.next)) {
                      case 0:
                        return (
                          $('.loading').show(),
                          (e.next = 3),
                          Ajax({ key: '3C502C97ABDA40D0A60FBEE50FAAD1DA' })
                        );
                      case 3:
                        (i = e.sent),
                          (a = i.data),
                          (s = a.end_update_time),
                          (n = a.hcount),
                          (o = a.mcount),
                          (r = a.highlist),
                          (c = a.middlelist),
                          (t.end_update_time = s),
                          (t.hcount = n),
                          (t.mcount = o),
                          (t.highlist = r),
                          (t.middlelist = c),
                          (t.loaded = !0),
                          $(t.$refs.page).paging({
                            pageNum: 1,
                            totalNum: Math.ceil(t.highlist.length / 10),
                            callback: function (e) {
                              (t.page = e), window.scrollTo(0, 370);
                            },
                          }),
                          $(t.$refs.page1).paging({
                            pageNum: 1,
                            totalNum: Math.ceil(t.middlelist.length / 10),
                            callback: function (e) {
                              (t.page1 = e),
                                window.scrollTo(0, 370),
                                $('.loading').show(),
                                setTimeout(function () {
                                  $('.loading').hide();
                                }, 200);
                            },
                          });
                      case 18:
                      case 'end':
                        return e.stop();
                    }
                }, e);
              })
            )();
          },
        },
        watch: {
          activeName: function (t) {
            'high' == t && (this.ajaxGetCount(), (this.page = 1)),
              'middle' == t && (this.ajaxGetCount(), (this.page1 = 1));
          },
        },
      },
      c = r,
      l = (i('5df0'), i('2877')),
      d = Object(l['a'])(c, s, n, !1, null, null, null),
      u = d.exports;
    i('063a');
    a['a'].config.productionTip = !1;
    new a['a']({
      render: function (t) {
        return t(u);
      },
    }).$mount('#app');
  },
})();
//# sourceMappingURL=risk.8d29703e.js.map
